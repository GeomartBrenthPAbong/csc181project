
var g_current_active_li;
var g_right_title;
var g_right_content;
var g_id;

var g_added_scripts = [];
g_added_scripts.push($('ul.menu li.active').attr('id'));

function success_func(res) {
    activate_modal(res.msg);
}

function error_func(){
    activate_modal('Something went wrong. Please contact the webmaster.');
}

function ajaxify(p_data, p_success_func, p_error_func, p_before_send, p_data_type) {
    if(!p_success_func)
        p_success_func = success_func;
    if(!p_error_func)
        p_error_func = error_func;

    if(!p_data_type)
        p_data_type = 'json';

    $.ajax({
            url: 'http://localhost/spam/ajax.py',
            dataType: p_data_type,
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

function get_styles(resources, callback){
        if(!resources){
            if(callback)
                callback();
            return;
        }

        var length = resources.length,
        idx = 0;

        for ( ; idx < length; idx++ )
            $('head').append($("<link rel='stylesheet' href='" +resources[idx]+ "' type='text/css' media='screen' />"))

        if (callback)
            callback();
    }

    var getScript = $.getScript;
    $.getScript = function( resources, callback ) {
        if(!resources){
            if(callback)
                callback();
            return;
        }

        var length = resources.length,
        handler = function() { counter++; },
        deferreds = [],
        counter = 0,
        idx = 0;

        for ( ; idx < length; idx++ ) {
            deferreds.push(
                getScript( resources[ idx ], handler )
            );
        }

        $.when.apply( null, deferreds ).then(function() {
            callback && callback();
        });
    };

    function change_content_animate(response, callback){
        $('.right-content').promise().done(function(){
            $('.right-bg').css('display', 'none');

            $('div.right-content h2.title').html(response.data.title);
            $('div.right-content div.wrapper div').html(response.data.right_content);

            $('.right-content').animate({
                    'margin-right': '0'
                }, 200, function(){
                    if(callback)
                            callback();
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

function change_page_content(response) {
        if(response.status == 'FAILED' && response.type == 'function_existence'){
            activate_modal('Error', response.msg);
            return;
        }
        else if(response.type != 'page_existence'){
            get_styles(response.data.css, function(){
                hide_right_content();
                change_content_animate(response, function(){
                    general_main();
                    if(response.data.js)
                        $.getScript(response.data.js);
                    else{
                        var fn_name = g_id + '_main()';

                        eval(fn_name);
                    }
                });
            });
        }
}

function hide_right_content(){
        g_right_title = $('div.right-content h2.title').text();
        g_right_content = $('div.right-content div.wrapper div').text();

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

      ajaxify(data, p_success_func, error_func);
}

function on_logout(response){
    if(response.status == 'SUCCESS')
        window.location = response.redirect_url;
    else
        activate_modal(response.msg);
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

function getNotifNo(){
        var data = {
            action: 'get_notif_no'
        }

        ajaxify(data, updateApptTab, function(){});
}


function updateApptTab(res){
        notifNo = res.msg
        if (notifNo > 0){
            $('#profstudmanageappt a span').empty().text("(" + notifNo + ")");
        }
        else
            $('#profstudmanageappt a span').remove();
}

$.ajaxSetup({ cache: true });

function general_main(){
    var rc_height = $('.right-content').height();
    var lc_height = $('.left-content').height();

    if(rc_height > lc_height)
        $('.left-content').height(lc_height);
    else
        $('.right-content').height(rc_height);
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
        else{
            var contents = ['right_content', 'title'];

            if($.inArray(g_current_active_li, g_added_scripts) == -1){
                contents.push('js');
                contents.push('css');

                g_added_scripts.push(g_current_active_li);
            }

            g_id = $(this).closest('li').attr('id');
            get_page_content(g_id, contents, change_page_content);
        }

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
