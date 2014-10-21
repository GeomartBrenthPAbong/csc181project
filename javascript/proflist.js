var page = 0;
var list_limit = 5;
var searchOn = false;
var modalOn = false;
var stud_name = "";
var body = "";
var footer = "";
var g_curr_schedules;
var g_selected_day;
var g_selected_prof_sched;
var g_selected_prof;
var g_msg;

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

function produce_time_ranges(p_ranges){
    var content = 'Select Time Range:';

    content += '<select required="required" name="range_selector">';
    for(var i=0; i<p_ranges.length; i++)
        content += '<option value="' +p_ranges[i][2]+ '">' +p_ranges[i][0] + ' - ' + p_ranges[i][1] + '</option>';
    content += '</select>';

    return content;
}
function sched_disp(res){
    if (res.status == 'SUCCESS'){
        head = 'You wish to make an appointment with ' + stud_name;
        content = "<br/>Please choose among your professor's available schedules: <br/><br/>";
        content += '<p id="day-options">Select Day:';

        content += '<select required="required" name="day_selector">';

        g_curr_schedules = [];
        g_curr_schedules[0] = null;
        g_curr_schedules[1] = null;
        g_curr_schedules[2] = null;
        g_curr_schedules[3] = null;
        g_curr_schedules[4] = null;
        g_curr_schedules[5] = null;
        g_curr_schedules[6] = null;

        var first_day = null;

        if(res.msg.mon && res.msg.mon.length > 0){
            first_day = 1;
            g_curr_schedules[1] = res.msg.mon;
            content += '<option value="1">Monday</option>';
        }
        if(res.msg.tue && res.msg.tue.length > 0){
            if(first_day == null)
                first_day = 2;
            g_curr_schedules[2] = res.msg.tue;
            content += '<option value="2">Tuesday</option>';
        }
        if(res.msg.wed && res.msg.wed.length > 0){
            if(first_day == null)
                first_day = 3;
            g_curr_schedules[3] = res.msg.wed;
            content += '<option value="3">Wednesday</option>';
        }
        if(res.msg.thu && res.msg.thu.length > 0){
            if(first_day == null)
                first_day = 4;
            g_curr_schedules[4] = res.msg.thu;
            content += '<option value="4">Thursday</option>';
        }
        if(res.msg.fri && res.msg.fri.length > 0){
            if(first_day == null)
                first_day = 5;
            g_curr_schedules[5] = res.msg.fri;
            content += '<option value="5">Friday</option>';
        }
        if(res.msg.sat && res.msg.sat.length > 0){
            if(first_day == null)
                first_day = 6;
            g_curr_schedules[6] = res.msg.sat;
            content += '<option value="6">Saturday</option>';
        }
        if(res.msg.sun && res.msg.sun.length > 0){
            if(first_day == null)
                first_day = 0;
            g_curr_schedules[0] = res.msg.sun;
            content += '<option value="0">Sunday</option>';
        }

        content += '</select></p><p id="time-ranges">' + produce_time_ranges(g_curr_schedules[first_day]) + '</p>';

        content += '<br/><br/>';
        content += 'Message: <br/><br/>';
        content += '<textarea id="msg-for-prof" placeholder="Leave a message for your professor..." rows="4" cols="60"></textarea><br/>';
        footer = '<button id="btn-back" type="button" class="btn btn-primary btn-large">Back</button>';
        footer += '<button id="select-date-appt" type="button" class="btn btn-primary btn-large">Submit</button>';
        activate_modal(head,content,footer);
    }
    else
        activate_modal('Error!', res.msg);
}

function get_eq_day(p_num){
        if(p_num == 0)
            return 'sun';
        else if(p_num == 1)
            return 'mon';
        else if(p_num == 2)
            return 'tue';
        else if(p_num == 3)
            return 'wed';
        else if(p_num == 4)
            return 'thu';
        else if(p_num == 5)
            return 'fri';
        else if(p_num == 6)
            return 'sat';
    }

function get_date_difference(p_date_1, p_date_2){
    var time_1 = p_date_1.getTime();
    var time_2 = p_date_2.getTime();

    return parseInt((time_2 - time_1)/(24*3600*1000));
}

function setup_appointment_success_func(response){
    if(response.status == 'SUCCESS')
        activate_modal('Congratulations!', 'You have successfully sent an appointment request to professor ' + response.msg.prof_name);
    else
        activate_modal('Error!', response.msg);
}

function inspect_date_selected(p_date){
    var date = new Date(p_date);
    var clicked_day = date.getDay();

    if(clicked_day != g_selected_day){
        $('#modal-body #notif-area').html('<p style="color: red;">Oopss! You said you want ' + get_eq_day(g_selected_day).toUpperCase()+'</p>');
        return false;
    }
    else if(get_date_difference(new Date(), new Date(p_date)) <= 0){
        $('#modal-body #notif-area').html('<p style="color: red;">Date must be in the future</p>');
        return false;
    }
    else{
        var data = {
           action: 'setup_appointment',
           prof_id: g_selected_prof,
           prof_sched: g_selected_prof_sched,
           date: p_date,
           msg: g_msg
        };

        ajaxify(data, setup_appointment_success_func);
    }

    return true;
}

function studhome_main(){
    var data = {
        action: 'gen_prof_list',
        limit: list_limit
    };

    $('#btn-prev').hide();
    ajaxify(data, gen_proflist_html);
}

jQuery(document).ready(function($) {

    $('#modal-body').on('change', 'select[name="day_selector"]', function(){
        var day = $(this).val();
        $('#modal-body #time-ranges').html(produce_time_ranges(g_curr_schedules[day]));
    });

    $('.right-content').on('click', '#proflist td a', function (e){
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
            g_selected_prof = curr_prof_id;
            var data = {
                action: 'gen_prof_sched',
                id: curr_prof_id
            };
            ajaxify(data,sched_disp);
        }
        else if (buttonid == 'select-date-appt'){
            g_selected_day = $('select[name="day_selector"]').val();
            g_selected_prof_sched = $('select[name="range_selector"]').val();
            g_msg = $('textarea#msg-for-prof').val();

            activate_modal('Select date', '<div id="notif-area"></div><div id="date-options"></div>');

            $('#modal-body #date-options').zabuto_calendar({
                cell_border: true,
                today: true,
                show_previous: false,
                show_next: 2,
                nav_icon: { prev: '<i class="fa fa-chevron-circle-left">&lt;&lt;</i>',
                            next: '<i class="fa fa-chevron-circle-right">&gt;&gt;</i>' },
                action: function () {
                    return inspect_date_selected($("#" + this.id).data("date")); },
              ajax: {
                  url: "show_data.php?action=1",
                  modal: false }
             });
        }
        else if (buttonid == 'btn-back'){

            var data = {
                action: 'gen_prof_details',
                data: curr_prof_id
            };

            ajaxify(data,gen_prof_profile);
        }
        e.preventDefault();
    });

    $('.right-content').on('click', '#btn-search', function (e){
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

    $('.right-content').on('click', '#btn-next', function (e){
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

    $('.right-content').on('click', '#btn-prev',function (e){
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

    studhome_main();

});