jQuery(document).ready( function($){
    $( 'a.test').click( function() {
        $.ajax({
            url: 'http://localhost/spam/ajax.py',
            dataType: 'json',
            traditional: true,
            async: false,
            type: 'POST',
            global: true,
            data: {
                'action_name': 'test_ajax',
                'the_value': 'sample value'
            },
            success: function( response ) {
                alert( response.msg );
            },
            error: function() {
                alert( 'Something went wrong!' );
            }
        });
    });
});