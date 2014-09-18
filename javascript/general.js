function success_func(res) {
    alert(res.msg);
}

function error_func(){
    alert('Something went wrong!');
}

function ajaxify(p_data, p_success_func, p_error_func) {
    if(!p_success_func)
        p_success_func = success_func;
    if(!p_error_func)
        p_error_func = error_func;

    $.ajax({
            url: 'http://localhost/spam/scripts/ajax.py',
            dataType: 'json',
            traditional: true,
            async: false,
            type: 'POST',
            global: true,
            data: p_data,
            success: function( response ) {
                p_success_func(response);
            },
            error: function() {
                p_error_func();
            }
        });
}
