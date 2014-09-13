jQuery(document).ready(function($){

    // Animation for showing the icon when the mouse hovered the menu item
    $('a.menu-item-link').hover(function(){
        if($(this).parent().parent().hasClass('active'))
            return;

        var nav_block = $(this).siblings('span.nav-block');

        nav_block.finish();
        nav_block.animate({
            'top': '-78%'
                          }, 500, function(){})
    }, function(){
        if($(this).parent().parent().hasClass('active'))
            return;
        var nav_block = $(this).siblings('span.nav-block');

        nav_block.animate({
            'top': '0%'
                          }, 300, function(){})
    });
});