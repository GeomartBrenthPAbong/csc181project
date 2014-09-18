jQuery(document).ready( function($){
    $( 'input[name=btnSubmit]').click( function(e) {
        var data = {
            action: 'test_ajax',
            username: $('input[name=email]').val(),
            password: $('input[name=password]').val()
        };

        ajaxify(data);

        e.preventDefault();
        e.stopPropagation();

        return false;
    });
});