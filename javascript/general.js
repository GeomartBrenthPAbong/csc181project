
var g_current_active_li;

function success_func(res) {
    alert(res.msg);
}

function error_func(){
    alert('Something went wrong. Please contact the webmaster.');
}

function ajaxify(p_data, p_success_func, p_error_func, p_before_send) {
    if(!p_success_func)
        p_success_func = success_func;
    if(!p_error_func)
        p_error_func = error_func;

    $.ajax({
            url: 'http://localhost/spam/ajax.py',
            dataType: 'json',
            traditional: true,
            async: false,
            type: 'POST',
            global: true,
            data: p_data,
            beforeSend: function(jqXHR, settings){
              if(p_before_send)
                   p_before_send();
            },
            success: function( response ) {
                p_success_func(response);
            },
            error: function() {
                p_error_func();
            }
        });
}

function is_time(p_str){
    if(!p_str)
        return false;


    return true;
}

function get_time_difference(p_from_time, p_to_time) {
    return p_to_time - p_from_time;
}

function change_page_content(response) {
    $('.right-content').promise().done(function(){
        $('.right-bg').css('display', 'none');

        $('div.right-content h2.title').html(response.data.title);
        $('div.right-content div.wrapper div').html(response.data.right_content);

        $('.right-content').animate({
                'margin-right': '0'
            }, 200, function(){
                $(this).animate({
                    'margin-right': '-100px'
                }, 400, function(){
                    $(this).animate({
                        'margin-right': '0'
                    }, 600);


                    var prev_active = $('ul.menu li.active').index();
                    var new_active = $('ul.menu li#' + g_current_active_li).index();

                    var counter = 1;
                    var i;
                    var len = $('ul.menu li').length;

                    if(new_active - prev_active > 0){
                        for(i = prev_active+1; i <= new_active + 1; i++){
                            (function(li){
                                setTimeout(function(){
                                    $('ul.menu li:nth-child(' +li+ ')').addClass('active');
                                },100*counter);

                                if(i != new_active +1){
                                    setTimeout(function(){
                                        $('ul.menu li:nth-child(' +li+ ')').removeClass('active');
                                    },100* (counter + len));
                                }
                            }(i));

                            counter++;
                        }
                    }
                    else{
                        for(i = prev_active+1; i > new_active; i--){
                            (function(li){
                                setTimeout(function(){
                                    $('ul.menu li:nth-child(' +li+ ')').addClass('active');
                                },100*counter);

                                if(i-1 != new_active) {
                                    setTimeout(function(){
                                        $('ul.menu li:nth-child(' +li+ ')').removeClass('active');
                                    },100* (counter + len));
                                }
                            }(i));

                            counter++;
                        }
                    }
                })
        });
    });
}

function hide_right_content(){
    $('.right-content').animate({
        'margin-right' : '-' + $(this).width()
    }, 600, function(){
        $('.right-bg').css('display', 'block');
    });
}

function get_page_content(p_page_name, p_locations, p_success_func){
    var data = {
          action: 'get_page_content',
          page_name: p_page_name,
          page_location: JSON.stringify(p_locations)
      }

      ajaxify(data, p_success_func, error_func, hide_right_content);
}

function on_logout(response){
    if(response.status == 'SUCCESS')
        window.location = response.redirect_url;
    else
        alert(response.msg);
}



function close_modal(){
    $('#blocker').css('display', 'none');
    $('#modal-container').css('display', 'none');
    $('#modal').css('display', 'none');
    $('#modal-holder').css('display', 'none');
}


function activate_modal(header, body, footer){
    $('#blocker').css('display', 'block');
    $('#modal-container').css('display', 'block');
    $('#modal').css('display', 'block');
    $('#modal-holder').css('display', 'block');

    if (!header)
        header = "";

    if (!body)
        body = "";

    if (!footer)
        footer = "";

    $('#modal-header').empty();
    $('#modal-body').empty();
    $('#modal-footer').empty();
    $('#modal-header').append(header);
    $('#modal-body').append('<b>' + body + '</b>');
    $('#modal-footer').append('<b>' + footer + '</b>');

    window_height = $(window).height();
    top_margin = (window_height/2)*.30;
    $('#modal').css('margin-top', top_margin);
}


jQuery(document).ready(function($){
    $('ul.menu li a').click(function(e){
        g_current_active_li = $(this).parent().attr('id');

        if(g_current_active_li == 'sign_out') {
            var data = {
                   action: 'logout'
               }

               ajaxify(data, on_logout);
        }
        else
            get_page_content($(this).closest('li').attr('id'), ['right_content', 'title'], change_page_content);

        e.preventDefault();
        e.stopPropagation();

        return false;
   });

   $('#modal-close').click(function(){
        close_modal();
   });

   $(document).keyup(function(e){
        if (e.keyCode == 27){
             close_modal();
        }   // esc
    });

});
