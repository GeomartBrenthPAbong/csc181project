page = 0;
list_limit = 5;
searchOn = false;
modalOn = false;

function gen_proflist_html(res){

    if (res.msg[0][0] != "None"){
        $('#page').show();
        $('#proflist').empty();


        for(var i = 0; i < res.msg.length; i++)
        {
            prof_rows = '<tr id=' + res.msg[i][0] + ' data-toggle="modal">';
            prof_rows += '<td>';
            prof_rows += '<a href="#rowlinkModal" style="color:black;" data-toggle="modal" class="noline"><b>' + res.msg[i][1] + ' ' + res.msg[i][2] + '</b></a>';
            prof_rows += '</td>';
            prof_rows += '<td>';
            prof_rows += '<b>' + res.msg[i][3] + '</b>';
            prof_rows += '</td>';
            prof_rows += '<td>';
            prof_rows += '<b>' + res.msg[i][4] + '</b>';
            prof_rows += '</td>';
            prof_rows += '</tr>';
            $('#proflist').append(prof_rows);
        }

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
        $('#proflist').append('<br><span style="color:red; font-weight:bold;">&nbsp;No results found.</span>');
        $('#btn-next').hide();
        if(page!=0)  $('#btn-prev').show();
        $('#page').hide();
    }
}

function go_search(){

}

jQuery(document).ready(function($) {

    $('#proflist').on('click', 'td a', function (e){
        id = $(this).closest('tr').attr('id');
        header = 'PROFESSOR PROFILE';
        message = '<b>This will show a professor profile with id: '+ id + '</b>';
        footer = '<b>Add a button to request for appointment.</b>'

        activate_modal(header, message);
        modalOn = true;

        e.preventDefault();
    });

    $('#btn-search').click(function (e){
        if (!$('#input-search').val()){
            searchOn = false;

            var data = {
                action: 'gen_prof_list',
                limit: list_limit
            }
        }else{
            searchOn = true;
            var data = {
                action: 'gen_prof_list',
                name: $('#input-search').val(),
                limit: list_limit
            }
        }

        ajaxify(data, gen_proflist_html);
        e.preventDefault();
    });

    $(document).keypress(function(e) {
        if(e.which == 13) {
            if (!$('#input-search').val()){
                searchOn = false;

                var data = {
                    action: 'gen_prof_list',
                    limit: list_limit
                }
            }else{
                searchOn = true;
                var data = {
                    action: 'gen_prof_list',
                    name: $('#input-search').val(),
                    limit: list_limit
                }
            }

            ajaxify(data, gen_proflist_html);
            e.preventDefault();
        }
    });

    $('#btn-next').click( function (e){
        page++;

        if(searchOn){
            var data = {
                action: 'gen_prof_list',
                name: $('#input-search').val(),
                limit: list_limit,
                offset: page * list_limit
            }
        }else{
            var data = {
                action: 'gen_prof_list',
                limit: list_limit,
                offset: page * list_limit
            }
        }


        ajaxify(data, gen_proflist_html);

        e.preventDefault();
    });

    $('#btn-prev').click( function (e){
        page--;

        if(searchOn){
            var data = {
                action: 'gen_prof_list',
                name: $('#input-search').val(),
                limit: list_limit,
                offset: page * list_limit
            }
        }else{
            var data = {
                action: 'gen_prof_list',
                limit: list_limit,
                offset: page * list_limit
            }
        }

        ajaxify(data, gen_proflist_html);
        e.preventDefault();
    });

    //prof search on load
    //
    var data = {
        action: 'gen_prof_list',
        limit: list_limit
    };

    $('#btn-prev').hide();
    ajaxify(data, gen_proflist_html);
});