page = 0;
list_limit = 5;

function gen_proflist_html(res){

    if (res.msg[0][0] != "None"){
        $('#page').show();
        $('#proflist').empty();
        $('#proflist').append('<p>');
        for(var i = 0; i < res.msg.length; i++)
            $('#proflist').append('<p id ='+ res.msg[i][0] + '><a href="#">' + res.msg[i][1] + ' ' + res.msg[i][2] + '</a></p>');
        $('#proflist').append('</p>');

        if(page == 0)
            $('#btn-prev').hide();
        else
            $('#btn-prev').show();

        if(res.msg.length < list_limit)
            $('#btn-next').hide();
        else
            $('#btn-next').show();

        $('#page').empty();
        $('#page').append('Page ' + (page + 1));

    }else{
        $('#proflist').empty();
        $('#proflist').append('No more results found.');
        $('#btn-next').hide();
        $('#page').hide();
    }
}

jQuery(document).ready(function($) {

    $('#proflist').on('click', 'p a', function(e){
        id = $(this).closest('p').attr('id');
        alert(id);

        e.preventDefault();
    });

    $('#btn-next').click( function (e){
        page++;
        var data = {
            action: 'gen_prof_list',
            limit: list_limit,
            offset: page * list_limit
        }

        ajaxify(data, gen_proflist_html);

        e.preventDefault();
    });

    $('#btn-prev').click( function (e){
        page--;
        var data = {
            action: 'gen_prof_list',
            limit: list_limit,
            offset: page * list_limit
        }

        ajaxify(data, gen_proflist_html);
        e.preventDefault();
    });

    //prof search on load
    var data = {
        action: 'gen_prof_list',
        limit: list_limit
    };

    $('#btn-prev').hide();
    ajaxify(data, gen_proflist_html);
});