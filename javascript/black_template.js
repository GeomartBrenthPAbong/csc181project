jQuery(document).ready(function($){
    var g_on_top = false;
    var g_container_on_top = false;
    var g_typing;

    $('.logo a').css('bottom', '100%');

    free_fall('.logo a', function(){
        logo_typing();
        g_typing = setInterval(logo_typing, 20000);
    });

    $('.arrow-left').css('display', 'block');

    //===== Some Functions
    function logo_typing(){
        var logo_items = $('.logo a').children();
        var strings = ['tudent ', 'rofessor ', 'ppointment ', 'anager'];
        var pace = 300;

        typing('#' + logo_items.eq(0).attr('id'),'S', strings[0], pace, true, function(){ return g_on_top; }, function(){
           typing('#' + logo_items.eq(1).attr('id'), ' P', strings[1], pace, true, function(){ return g_on_top; }, function(){
               typing('#' + logo_items.eq(2).attr('id'), ' A', strings[2], pace, true, function(){ return g_on_top; }, function(){
                   typing('#' + logo_items.eq(3).attr('id'), ' M', strings[3], pace, true, function(){ return g_on_top; });
               })
           });
        });
    }

    //===== Effects
    function free_fall(p_selector, p_func_after){
       $(p_selector).animate({
           'bottom': '0%'
          },
          400,
          function(){
            $(this).animate({
                'margin-bottom': '80px'
                },
                300,
                function(){
                    $(this).animate({
                        'margin-bottom': '20px'
                        }, 600, p_func_after);
                })
        });
    }

    function typing(p_selector, p_start, p_string, p_pace,  p_return, p_extra_cond, p_callback){
        if(!p_selector || !$(p_selector) || !p_string)
            return;

        if(!p_pace)
            p_pace = 400;

        if(p_extra_cond && p_extra_cond())
            return;

        var text_holder = $(p_selector);
        var orig_string = text_holder.text();
        var current_pos = 0;

        text_holder.text(p_start);

        var timer = setInterval(function(){
            text_holder.append(p_string[current_pos]);

            if(current_pos++ == p_string.length || (
                p_extra_cond && p_extra_cond())) {
                clearInterval(timer);

                if(p_return)
                    text_holder.text(orig_string);

                if(p_callback)
                    p_callback();
            }
        },p_pace);
    }

    //===== Event Handlers

    //== Handle hide content

    $('.arrow-left').click(function(){
        $('.left-content').animate({
            'margin-left': '-30%'
        },600, function(){
            $('.right-content').animate({
                'width': '100%'
            },400, function(){
                var right_bg = $('.right-content .right-bg');

                $('.arrow-left').css('display', 'none');
                $('.arrow-right').css('display', 'block');

                right_bg.css('width', '100%');
                right_bg.css('margin-right', '0%');
            });
        })
    });

    $('.arrow-right').click(function(){
        var right_bg = $('.right-content .right-bg');

        right_bg.css('width', '70%');
        right_bg.css('margin-right', '30%');
        $('.right-content').animate({
            'width': '70%'
        },400, function(){
            $('.left-content').animate({
                'margin-left': '0'
            },400, function(){
                $('.arrow-left').css('display', 'block');
                $('.arrow-right').css('display', 'none');
            });
        })
    });

    //== Handle menu-item hovers

    $('ul.menu li a').hover(function(){
        $(this).finish();
        $(this).animate({
            'padding-top': '28px'
                        },500);
    }, function(){
        $(this).finish();
        $(this).animate({
            'padding-top': '50px'
                        },200);
    });

    //== Handle logo animations

    // logo free fall
    $(window).scroll(function(){
        var diff = $('#content').offset().top - $(this).scrollTop();

        if(!(g_on_top || g_container_on_top) && diff <= 90){
            var spam_container = $('.logo');
            var content = $('#content');
            var spam = $('.logo a');

            content.css('margin-top', '180px');

            spam.finish();
            spam_container.css('position', 'fixed');
            spam_container.css('margin-top', '-90px');

            spam.css('position', 'fixed');
            spam.css('bottom', '100%');
            spam.css('margin-bottom', '-67px');

            clearInterval(g_typing);

            g_on_top = true;
            g_container_on_top = true;
        }

        if(g_container_on_top && diff > 90){
            var spam_container = $('.logo');
            var content = $('#content');

            spam_container.css('position', 'relative');
            spam_container.css('margin-top', '0px');

            content.css('margin-top', '0px');

            g_container_on_top = false;
        }

        if(g_on_top && diff >= 180) {
            var spam = $('.logo a');

            spam.css('position', 'absolute');

            free_fall('.logo a', function(){
                g_typing = setInterval(logo_typing, 20000);
            });

            g_on_top = false;
        }
    });
});