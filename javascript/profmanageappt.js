page = 0;
list_limit = 5;
cur_appt_id = "";
onload_stat = "";
btn_id = "";
stud_name = "";
id = "";
footer = "";

function gen_appointment_list_html(res){
    if (res.msg.length > 0){

        $('#page').show();
        $('#apptlist').empty();

        for(var i = 0; i < res.msg.length; i++)
        {
            appt_rows = '<tr id=' + res.msg[i].appt_id + 'data-toggle="modal">';
            appt_rows += '<td>';
            appt_rows += '<b>' + res.msg[i].stud_name + '</b>';
            appt_rows += '</td>';
            appt_rows += '<td>';
            appt_rows += '<b>' + res.msg[i].sched_from_time + '</b>';
            appt_rows += '</td>';
            appt_rows += '<td>';
            appt_rows += '<b>'+res.msg[i].app_date+'</b>';
            appt_rows += '</td>';
            appt_rows += '<td>';
            appt_rows += '<a href="#rowlinkModal" data-toggle="modal" class="noline"><b> More...';
            appt_rows +=  '</b></a>'
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
        id += res.msg[0][1] + '<br/>';
        id += 'ID No.:';
        id += res.msg[0][2] + '<br/>';
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

function changeStat(){

    if (btn_id == 'Confirmed')
        alert("You've successfully confirmed your appointment with "+stud_name);
    else if (btn_id == 'Declined')
        alert("You've declined this appointment with " + stud_name);
    else if (btn_id == 'Cancel')
        alert ("You've cancelled your appointment with " + stud_name);

    close_modal();
    onload(onload_stat);
}

function onload(onload_stat){

    var data = {
        action: 'gen_appt_list',
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
            action: 'gen_appt_details',
            appt_id: cur_appt_id
        };
        ajaxify(data, gen_appt_details_html);

        e.preventDefault();

    });

    $('#modal-footer').on('click','button', function (e){

       btn_id = $(this).attr('id');

       if(btn_id == "Cancel") bton_id = "Declined";
       else bton_id = btn_id;

        var data = {

               action: 'change_status',
               appt_id: cur_appt_id,
               stat: bton_id

           }


        ajaxify(data, changeStat);
    });

    $('.btn-page').on('click','button', function (e){
        buttonid = $(this).attr('id');

        if (buttonid == 'btn-next')
            page++;
        else if(buttonid == 'btn-prev')
            page--;

        var data = {

            action: 'gen_appt_list',
            limit: list_limit,
            offset: page * list_limit,
            stat: onload_stat

        };

        ajaxify(data, gen_appointment_list_html);
        e.preventDefault();

    });

    $('.btn-gen').on('click','button', function (e){
        button_id = $(this).attr('id');
        if (button_id == 'btn-approved'){

            page = 0;
            onload_stat = 'Confirmed';

            document.getElementById('btn-approved').disabled = true;
            document.getElementById('btn-pending').disabled = false;

        }
        else if (button_id == 'btn-pending'){

            page = 0;
            onload_stat = 'Pending';

            document.getElementById('btn-approved').disabled = false;
            document.getElementById('btn-pending').disabled = true;

        }
        var data = {

                action: 'gen_appt_list',
                limit: list_limit,
                stat: onload_stat


        }
        document.getElementById('appt-stat').textContent = onload_stat + " Appointments List";
        ajaxify(data, gen_appointment_list_html);
        e.preventDefault();
    });

    //appointment search on load
    onload('Pending');

});