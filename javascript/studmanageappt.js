page = 0;
list_limit = 2;
count = 0;
var status;

function gen_appointment_list_html(res){
    if (res.msg[0][0] != "None"){
        $('#page').show();
        $('#apptlist').empty();


        for(var i = 0; i < res.msg.length; i++)
        {
            appt_rows = '<tr id=' + res.msg[i][0] + ' data-toggle="modal">';
            appt_rows += '<td>';
            appt_rows += '<a href="#rowlinkModal" data-toggle="modal" class="noline"><b>' + res.msg[i][2] +  '</b></a>';
            appt_rows += '</td>';
            appt_rows += '<td>';
            appt_rows += '<b>' + res.msg[i][4] + '</b>';
            appt_rows += '</td>';
            appt_rows += '<td>';
            appt_rows += '<b>'+res.msg[i][5]+'</b>';
            appt_rows += '</td>';
            appt_rows += '<td>';
            appt_rows += '<b>'+res.msg[i][6]+'</b>';
            appt_rows += '</td>';
            appt_rows += '<td>';
            appt_rows += '<b><button id="btn-more"';
            appt_rows += '" type="button" class="btn btn-primary btn-large" style="font-weight: bold;">'+'More...'+'</button></b>';
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
        $('#apptflist').append('<br><span style="color:black; font-weight:bold;">&nbsp;No results found.</span>');
        $('#btn-next').hide();
        $('#page').hide();
    }
}
function appt_modal_html(res){


}
jQuery(document).ready(function($) {
    $('#apptlist').on('click', 'td a', function(e){
        id = $(this).closest('tr').attr('id');
        alert(id);

        e.preventDefault();
    });
    $('#btn-more').click(function(e){
      activate_modal('Header','Body','Footer');
      e.preventDefault();
    });
    $('#btn-next').click( function (e){
        page++;
        if (count>0) status = 'Confirmed';
        else if (count<0) status = 'Pending';
        else if (count=0) status = 'Declined';
        var data = {
            action: 'gen_appt_list',
            limit: list_limit,
            offset: page * list_limit,
            stat: status
        };

        ajaxify(data, gen_appointment_list_html);
        e.preventDefault();
    });

    $('#btn-prev').click( function (e){
        page--;
        if (count>0) status = 'Confirmed';
        else if (count<0) status = 'Pending';
        else if (count=0) status = 'Declined';
        var data = {
            action: 'gen_appt_list',
            limit: list_limit,
            offset: page * list_limit,
            stat: status
        }
        ajaxify(data, gen_appointment_list_html);
        e.preventDefault();
    });
    $('#btn-approved').click( function (e){
        page = 0;
        count++;
        var data = {
            action: 'gen_appt_list',
            limit: list_limit,
            stat: 'Confirmed'

        }
        document.getElementById('btn-approved').disabled = true;
        document.getElementById('btn-pending').disabled = false;
        document.getElementById('btn-declined').disabled = false;
        document.getElementById('appt-stat').textContent = "Confirmed Appointments List";
        ajaxify(data, gen_appointment_list_html);
        e.preventDefault();
    });
    $('#btn-declined').click( function (e){
        page = 0;
        count = 0;
        var data = {
            action: 'gen_appt_list',
            limit: list_limit,
            stat: 'Declined'

        }
        document.getElementById('btn-approved').disabled = false;
        document.getElementById('btn-pending').disabled = false;
        document.getElementById('btn-declined').disabled = true;
        document.getElementById('appt-stat').textContent = "Declined Appointments List";
        ajaxify(data, gen_appointment_list_html);
        e.preventDefault();
    })

    $('#btn-pending').click( function (e){
        page = 0;
        count--;
        var data = {
            action: 'gen_appt_list',
            limit: list_limit,
            stat: 'Pending'

        }
        document.getElementById('btn-approved').disabled = false;
        document.getElementById('btn-pending').disabled = true;
        document.getElementById('btn-declined').disabled = false;
        document.getElementById('appt-stat').textContent = "Pending Appointments List";
        ajaxify(data, gen_appointment_list_html);
        e.preventDefault();
    })

    //appt search on load
    var data = {
        action: 'gen_appt_list',
        limit: list_limit,
        stat: 'Pending'
    };
    document.getElementById('btn-approved').disabled = false;
        document.getElementById('btn-pending').disabled = true;
        document.getElementById('btn-declined').disabled = false;
    document.getElementById('appt-stat').textContent = "Pending Appointments List";
    $('#btn-prev').hide();
    ajaxify(data, gen_appointment_list_html);
});