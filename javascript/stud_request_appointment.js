jQuery(document).ready(function($) {

    $('#btn-modal').click(function(e){
        activate_modal('Header','Body','Footer');
        e.preventDefault();
    });

});