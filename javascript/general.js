jQuery(document).ready( function($) {
    var color = true;
    setInterval( justASimpleEffects, 1000 );

    function justASimpleEffects() {
        if(color)
            $('#content').css( 'background-color', '#C2BFBF');
        else
            $('#content').css( 'background-color', '#FFFFFF');
        color = !color;
    }
});

