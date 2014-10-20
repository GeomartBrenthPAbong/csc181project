var g_page = 0;
var g_cur_appt_id = "";
var g_onload_stat = "";
var g_btn_id = "";
var g_stud_name = "";
var g_list_limit = 5;
var g_id = "";
var g_footer = "";

function gen_appointment_list_html(res){
    if (res.status == 'SUCCESS'){

        $('#page').show();
        $('#apptlist').empty();

        for(var i = 0; i < res.msg.length; i++)
        {
            appt_rows = '<tr id=' + res.msg[i].appt_id + ' data-toggle="modal">';
            appt_rows += '<td>';

            if( res.msg[i].curr_user_type == 'Professor')
                appt_rows += '<b>' + res.msg[i].stud_name + '</b>';
            else
                appt_rows += '<b>' + res.msg[i].prof_name + '</b>';

            appt_rows += '</td>';
            appt_rows += '<td>';
            appt_rows += '<b>' + res.msg[i].sched_from_time + ' - ' + res.msg[i].sched_to_time+ '</b>';
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

        if(g_page == 0)
            $('#btn-prev').hide();
        else
            $('#btn-prev').show();

        if(res.msg.length <  g_list_limit)
            $('#btn-next').hide();
        else
            $('#btn-next').show();

        $('#page').empty();
        $('#page').append('Page ' + (g_page + 1));

    }else{

        $('#apptlist').empty();
        $('#apptlist').append('<br><span style="color:red; font-weight:bold;">&nbsp;' +res.msg+ '</span>');
        $('#btn-next').hide();

        if (g_page!=0){
            $('#btn-prev').show();
        }

        $('#page').hide();
    }
}

function gen_appt_details_html(res){
    if (res.status == 'SUCCESS'){
        var body;
        body = '<table>';
        if(res.msg[0][9] == 'Professor'){
            body += '<tr><td class="stud-name">Student:</td>';
            body += '<td>' + res.msg[0][1] + '</td></tr>';
        }
        else{
            body += '<tr><td class="prof-name">Professor:</td>';
            body += '<td>' + res.msg[0][0] + '</td></tr>';
        }

        body += '<tr><td class="id-num">ID No.:</td>';

        if(res.msg[0][9] == 'Professor')
            body += '<td>' + res.msg[0][2] + '</td></tr>';
        else
            body += '<td>' + res.msg[0][10] + '</td></tr>';

        if(res.msg[0][9] == 'Professor'){
            body += '<tr><td class="stud-course">Course:</td>';
            body += '<td>' + res.msg[0][3] + '</td></tr>';
        }

        body += '<tr><td class="sched-range">Schedule Range:</td>';
        body += '<td>' + res.msg[0][4] + ' to ' + res.msg[0][5] + '</td></tr>';
        body += '<tr><td class="req-date">Requested Date:</td>';
        body += '<td>' + res.msg[0][6] + '</td></tr>';
        body += '<tr><td class="app-msg">Message:</td>';
        body += '<td>' + res.msg[0][7] + '</td></tr>';
        body += '<tr><td class="app-stat">Status:</td>';
        body += '<td>' + res.msg[0][8] + '</td></tr>';
        body += '</table>';

        g_stud_name = res.msg[0][1];
        if (res.msg[0][9] == 'Professor' && res.msg[0][8]=='Pending'){

            g_footer = '<div id = "modal-div" style="margin-left:15px; margin-top:10px; padding: 10px;">';
            g_footer += '<table style="width:50%; margin: 0 auto;"><tr><td>';
            g_footer += '<button id="Confirmed" type="button" class="btn btn-primary btn-large">Confirm</button>';
            g_footer += '</td><td>';
            g_footer += '<button id="Declined" type="button" class="btn btn-primary btn-large">Decline</button>';
            g_footer += '</td></tr></table>';
        }
        else if(res.msg[0][9] == 'Professor'){
            g_footer = '<div id = "modal-div" style="margin-left:400px; margin-top:10px; padding: 10px;">';
            g_footer += '<button id="Cancel" type="button" class="btn btn-primary btn-large">Cancel this Appointment</button></div>';
        }

        activate_modal("Appointment Details",body, g_footer);
    }
    else
        activate_modal('Error!', res.msg);
}

function changeStat(response){
    if(response.status == 'SUCCESS'){
        $('#apptlist tr#' + g_cur_appt_id).remove();
        if (g_btn_id == 'Confirmed')
            activate_modal("You've successfully confirmed your appointment with " + response.msg.stud_name);
        else if (g_btn_id == 'Declined')
            activate_modal("You've declined this appointment with " + response.msg.stud_name);
        else if (g_btn_id == 'Cancel')
            activate_modal("You've cancelled your appointment with " + response.msg.stud_name);
    }
    else
        activate_modal('Error!', response.msg);
}

function onload(g_onload_stat){
    var data = {
        action: 'gen_appt_list',
        limit: g_list_limit,
        offset: g_page * g_list_limit,
        stat: g_onload_stat
    };

    if (g_onload_stat == 'Pending'){
        document.getElementById('btn-approved').disabled = false;
        document.getElementById('btn-pending').disabled = true;
    }
    else {
        document.getElementById('btn-approved').disabled = true;
        document.getElementById('btn-pending').disabled = false;
    }

    document.getElementById('appt-stat').textContent = g_onload_stat + " Appointments List";

    $('#btn-prev').hide();

    ajaxify(data, gen_appointment_list_html);
}

function profstudmanageappt_main() {
       onload('Pending');
}

jQuery(document).ready(function($) {
    $('.right-content').on('click', '#apptlist td a', function(e){
        g_cur_appt_id = $(this).closest('tr').attr('id');

        var data = {
            action: 'gen_appt_details',
            appt_id: g_cur_appt_id
        };
        ajaxify(data, gen_appt_details_html);

        e.preventDefault();

    });

    $('#modal-footer').on('click',' button', function (e){
       var bton_id;
       g_btn_id = $(this).attr('id');

       if(g_btn_id == "Cancel") bton_id = "Declined";
       else bton_id = g_btn_id;

        var data = {
               action: 'change_status',
               appt_id: g_cur_appt_id,
               stat: bton_id
           };

        ajaxify(data, changeStat);
    });

    $('.right-content').on('click','#btn-page button', function (e){
        buttonid = $(this).attr('id');

        if (buttonid == 'btn-next')
            g_page++;
        else if(buttonid == 'btn-prev')
            g_page--;

        onload(g_onload_stat);
        e.preventDefault();

    });

    $('.right-content').on('click','#btn-gen button', function (e){
        button_id = $(this).attr('id');
        if (button_id == 'btn-approved'){
            g_page = 0;
            g_onload_stat = 'Confirmed';
        }
        else if (button_id == 'btn-pending'){
            g_page = 0;
            g_onload_stat = 'Pending';
        }

        onload(g_onload_stat);
        e.preventDefault();
    });

    profstudmanageappt_main();
});