page = 0;
list_limit = 5;
searchOn = false;
modalOn = false;
stud_name = "";
body = "";
footer = "";

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

function gen_prof_profile(res){
    if (res.msg[0][0]!="None"){


        body = 'ID No.:';
        body += res.msg[0][0] + '<br/>';
        body += 'College: ';
        body += res.msg[0][1] + '<br/>';
        body += 'Department: ';
        body += res.msg[0][2] + '<br/>';
        body += 'E-mail address: ';
        body += res.msg[0][3] + '<br/>';
        body += 'Address: ';
        body += res.msg[0][4] + '<br/>';
        body += 'Phone Number: ';
        body += res.msg[0][5] + '<br/>';

        stud_name = res.msg[0][6] + ' ' + res.msg[0][7];
        id = res.msg[0][1];
        footer = '<div id = "modal-div" style="margin-left:15px; margin-top:10px; padding: 10px;">';
        footer += '<button id="make-appt" type="button" class="btn btn-primary btn-large">Make an appointment</button></div>';

    }
        activate_modal("Professor " + stud_name, body, footer);
       // modalOn = true;


}
function sched_disp(res){

    if (res.msg[0][0] != "None"){
        head = 'You wish to make an appointment with ' + stud_name;
        content = "<br/>Please choose among your professor's available schedules: <br/><br/>"
        content += '<select required="required" name = "sched_selector">';

        for (var i=0; i<res.msg.length; i++){

           content += '<option value="' + res.msg[i][5] + '">';
           content += res.msg[i][4] + ', ';
           content += res.msg[i][2] + ' - ';
           content += res.msg[i][3];
           content += '</option>';
           $('#schedlist').append(content);

        }
        content += '</select><br/><br/>';
        content += 'Message: <br/><br/>';
        content += '<textarea placeholder="Leave a message for your professor..." rows="4" cols="60"></textarea><br/>';
        footer = '<button id="submit-appt" type="button" class="btn btn-primary btn-large">Submit</button>';
        activate_modal(head,content,footer);
    }
    else{
        content = 'Professor ' + stud_name + ' has no available schedule as of the moment.';
        alert(content);
    }

}

jQuery(document).ready(function($) {

    $('#proflist').on('click', 'td a', function (e){
        id = $(this).closest('tr').attr('id');
        curr_prof_id = id;
        var data = {
            action: 'gen_prof_details',
            data: id
        };

        ajaxify(data,gen_prof_profile);
        e.preventDefault();
    });
    $('#modal-footer').on('click','button', function (e){
        buttonid = $(this).attr('id');

        if (buttonid == 'make-appt'){
            var data = {
                action: 'gen_prof_sched',
                id: curr_prof_id
            };
        ajaxify(data,sched_disp);
        }
        else if (buttonid == 'submit-appt'){
            var data = {
                action: create_appt,
                value:id /* TO EDIT!!!!!!!!!!!!!!!!!!!!!!!!*/
            }
        }
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