page = 0;
list_limit = 3;
count = 0;
var status;
cur_appt_id = "";
onload_stat = "Pending";
btn_id = "";
stud_name = "";

function gen_appointment_list_html(res){

    if (res.msg[0][0] != "None"){

        $('#page').show();
        $('#apptlist').empty();

        for(var i = 0; i < res.msg.length; i++)
        {
            appt_rows = '<tr id=' + res.msg[i][4] + ' data-toggle="modal">';
            appt_rows += '<td>';
            appt_rows += '<b>' + res.msg[i][0] + ' ' + res.msg[i][1] + '</b>';
            appt_rows += '</td>';
            appt_rows += '<td>';
            appt_rows += '<b>' + res.msg[i][3] + '</b>';
            appt_rows += '</td>';
            appt_rows += '<td>';
            appt_rows += '<b>'+res.msg[i][2]+'</b>';
            appt_rows += '</td>';
            appt_rows += '<td>';
            appt_rows += '<a href="#rowlinkModal" data-toggle="modal" class="noline"><b> More...';
            appt_rows +=  '</b></a>';
            appt_rows += '</td>';
            appt_rows += '</tr>';
            $('#apptlist').append(appt_rows);
        }

        if(page == 0)
            $('#btn-prev').hide();
        else
            $('#btn-prev').show();

        if(res.msg.length <  list_limit)
            $('#btn-next').hide();
        else
            $('#btn-next').show();

        $('#page').empty();
        $('#page').append('Page ' + (page + 1));

    }else{
        $('#apptlist').empty();
        $('#apptlist').append('<br><span style="color:red; font-weight:bold;">&nbsp;No results found.</span>');
        $('#btn-next').hide();

        if (page!=0){
            $('#btn-prev').show();
        }

        $('#page').hide();
    }
}
function gen_appt_details_html(res){

    if (res.msg[0][0]!="None"){

        id = 'Student: ';
        id += res.msg[0][1] + ' ' + res.msg[0][2] + '<br/>';
        id += 'ID No.:';
        id += res.msg[0][0] + '<br/>';
        id += 'Course: ';
        id += res.msg[0][3] + '<br/>';
        id += 'Schedule Range: ';
        id += 'From ' + res.msg[0][4] + ' to ' + res.msg[0][5] + '<br/>';
        id += 'Requested Date: ';
        id += res.msg[0][6] + '<br/>';
        id += 'Message: ';
        id += res.msg[0][7] + '<br/>';
        id += 'Status: ';
        id += res.msg[0][8];

        stud_name = res.msg[0][1] + ' ' + res.msg[0][2];

        if (res.msg[0][8]=='Pending'){

            footer = '<div id = "modal-div" style="margin-left:15px; margin-top:10px; padding: 10px;">';
            footer += '<button id="Confirmed" type="button" class="btn btn-primary btn-large">Confirm</button>';
            footer += '<button id="Declined" type="button" class="btn btn-primary btn-large">Decline</button></div>';

        }
        else{

            footer = '<div id = "modal-div" style="margin-left:400px; margin-top:10px; padding: 10px;">';
            footer += '<button id="Cancel" type="button" class="btn btn-primary btn-large">Cancel this Appointment</button></div>';

        }

        activate_modal("Appointment Details", id, footer);

    }
}

function changeStat(res){

    if (btn_id == 'Confirmed')
        alert("You've successfully confirmed your appointment with "+stud_name);
    else if (btn_id == 'Declined')
        alert("You've declined this appointment with " + stud_name);
    else if (btn_id == 'Cancel')
        alert ("You've cancelled your appointment with" + stud_name);

    close_modal();
    onload(onload_stat);
}
function onload(onload_stat){

    var data = {
        action: 'gen_appt_list_prof',
        limit: list_limit,
        stat: onload_stat
    };

    if (onload_stat == 'Pending'){
        document.getElementById('btn-approved').disabled = false;
        document.getElementById('btn-pending').disabled = true;
    }
    else {
        document.getElementById('btn-approved').disabled = true;
        document.getElementById('btn-pending').disabled = false;
    }

    document.getElementById('appt-stat').textContent = onload_stat + " Appointments List";

    $('#btn-prev').hide();

    ajaxify(data, gen_appointment_list_html);
}

jQuery(document).ready(function($) {

    $('#apptlist').on('click', 'td a', function(e){

        id = $(this).closest('tr').attr('id');
        cur_appt_id = id;

        var data = {
            action: 'gen_appt_details_prof',
            appt_id: id
        }
        ajaxify(data, gen_appt_details_html)

        e.preventDefault();

    });

    $('#modal-footer').on('click','button', function (e){

       btn_id = $(this).attr('id');

       if (btn_id == 'Confirmed'){
           var data = {

               action: 'change_status',
               appt_id: cur_appt_id,
               stat: 'Confirmed'

           }
       }
       else{
            var data = {

                action: 'change_status',
                appt_id: cur_appt_id,
                stat: 'Declined'

            }

        }

        ajaxify(data, changeStat);
    });

    $('#btn-next').click( function (e){

        page++;

        if (count=0) status = 'Confirmed';
        else status = 'Pending';

        var data = {

            action: 'gen_appt_list_prof',
            limit: list_limit,
            offset: page * list_limit,
            stat: status

        };

        ajaxify(data, gen_appointment_list_html);
        e.preventDefault();
    });

    $('#btn-prev').click( function (e){

        page--;

        if (count=0) status = 'Confirmed';
        else status = 'Pending';

        var data = {

            action: 'gen_appt_list_prof',
            limit: list_limit,
            offset: page * list_limit,
            stat: status

        }

        ajaxify(data, gen_appointment_list_html);
        e.preventDefault();

    });

    $('#btn-approved').click( function (e){

        page = 0;
        count=1;
        onload_stat = 'Confirmed';

        var data = {

            action: 'gen_appt_list_prof',
            limit: list_limit,
            stat: onload_stat


        }

        document.getElementById('btn-approved').disabled = true;
        document.getElementById('btn-pending').disabled = false;
        document.getElementById('appt-stat').textContent = "Confirmed Appointments List";

        ajaxify(data, gen_appointment_list_html);
        e.preventDefault();
    });

    $('#btn-pending').click( function (e){

        page = 0;
        count=0;
        onload_stat = 'Pending';

        var data = {


            action: 'gen_appt_list_prof',
            limit: list_limit,
            stat: onload_stat

        }

        document.getElementById('btn-approved').disabled = false;
        document.getElementById('btn-pending').disabled = true;
        document.getElementById('appt-stat').textContent = "Pending Appointments List";

        ajaxify(data, gen_appointment_list_html);
        e.preventDefault();
    });

    //appointment search on load
    onload(onload_stat);

});