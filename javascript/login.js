jQuery(document).ready(function($){
    function login_success_func(response){
        if(response.status == 'SUCCESS')
            window.location = response.redirect_url;
        else
            alert(response.msg);
    }

    $('input[name=btnSubmit]').click( function(e) {
        var data = {
            action: 'login',
            username: jQuery('input[name=id_number]').val(),
            password: jQuery('input[name=password]').val()
        };

        ajaxify(data, login_success_func);

        e.preventDefault();
        e.stopPropagation();

        return false;
    });
})

