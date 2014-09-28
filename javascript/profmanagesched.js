jQuery(document).ready(function($){
    var g_no_schedules = ($('#schedules p.warn'));

    //===== Functions
    function convertFrom24to12TimeFormat(p_time) {
        var time_hour = parseInt(p_time.substr(0,2));
        var time;

        if(time_hour > 12)
                time = sprintf('%02d', (time_hour - 12)) + p_time.substr(2) + ' pm'
            else
                time = p_time + ' am'
        return time
    }

    function add_sched_success_func(response){
        if(response.status == 'SUCCESS') {

            var from_time = convertFrom24to12TimeFormat(response.data.from_time);
            var to_time = convertFrom24to12TimeFormat(response.data.to_time);

            var schedule = '<tr id="' +response.data.id+ '">' +
                        '<td class="from-time">' + from_time + ' ' + '</td>' +
                        '<td class="to-time">' + to_time + ' ' + '</td>' +
                        '<td class="day">' + response.data.day + ' ' + '</td>' +
                        '<td class="actions"><a href="#" class="edit">Edit</a></td>' +
                        '<td class="actions"><a href="#" class="delete">Delete</a></td>' +
                    '</tr>';

            $('#schedules table').append(schedule);
        }
        else
            alert(response.msg);
    }

    //===== Event handlers
    $('input[name=btnAddSched]').click(function(e){
        if(!$.isNumeric($('select[name=from-time-hour]').val()) ||
           !$.isNumeric($('select[name=from-time-min]').val()) ||
           !$.isNumeric($('select[name=to-time-hour]').val()) ||
           !$.isNumeric($('select[name=to-time-min]').val())){
            e.preventDefault();
            e.stopPropagation();
            return false;
        }

        var from_time = (parseInt($('select[name=from-time-hour]').val()) * 100) + (parseInt($('select[name=from-time-min]').val()))
        var to_time = (parseInt($('select[name=to-time-hour]').val()) * 100) + (parseInt($('select[name=to-time-min]').val()))

        if($('select[name=from-time-m]').val() == 'pm')
           from_time += 1200

        if($('select[name=to-time-m]').val() == 'pm')
           to_time += 1200

        if(get_time_difference(from_time, to_time) <= 0) {
            alert('To time must be greater than the from time');
            e.preventDefault();
            e.stopPropagation();
            return false;
        }

        if(g_no_schedules){
            $('#schedules p.warn').remove();
            $('#schedules').append('<table><tr>' +
										'<td>From Time</td>' +
										'<td>To Time</td>' +
										'<td>Day</td>' +
										'<td colspan="2">Action</td>' +
									'</tr></table>');

            g_no_schedules = false;
        }

        var day = $('select[name=day]').val()

        var from_time_str = sprintf('%04d', from_time)
        var to_time_str = sprintf('%04d', to_time)

        from_time_str = from_time_str.substr(0, 2) + ':' + from_time_str.substr(2, 2);
        to_time_str = to_time_str.substr(0, 2) + ':' + to_time_str.substr(2, 2);

        var data = {
            action: 'add_schedule',
            from_time: from_time_str,
            to_time: to_time_str,
            day: day
        }
        ajaxify(data, add_sched_success_func);

        e.preventDefault();
        e.stopPropagation();
        return false;
    });

    function get_sched_editor(p_from_hour, p_from_min, p_from_m, p_to_hour, p_to_min, p_to_m) {
        var schedule_editor = $('#schedule-adder form').clone(true);

        schedule_editor.children('tbody tr td').last().remove();
        schedule_editor.children('tbody tr').append('<td><input type="submit" value="Save" class="save"/></td>');
        schedule_editor.children('tbody tr').append('<td><input type="submit" value="Cancel" class="cancel"/></td>');

        return schedule_editor.html();
    }

    $('#schedules').on('click', 'table tr td a.edit', function(e){
        var tr = $(this).parent().parent();
        var from_time_str = tr.children('td.from-time').text().trim();
        var to_time_str = tr.children('td.to-time').text().trim();
        var day = tr.children('td.day').text().trim();

        var from_time_hour = from_time_str.substr(0, 2);
        var from_time_min = from_time_str.substr(3, 2);
        var from_time_m = from_time_str.slice(-2).toLowerCase();

        var to_time_hour = to_time_str.substr(0, 2);
        var to_time_min = to_time_str.substr(3, 2);
        var to_time_m = to_time_str.slice(-2).toLowerCase();

        if(!$.isNumeric(from_time_hour) || !$.isNumeric(from_time_min) ||
           !$.isNumeric(to_time_hour) || !$.isNumeric(to_time_min)) {
            alert('Please don\'t change the values.');
            e.preventDefault();
            return false;
        }

        if(!((from_time_m == 'am' || from_time_m == 'pm') && (to_time_m == 'am' || to_time_m == 'pm'))){
            alert('Please don\'t change the values.');
            e.preventDefault();
            return false;
        }

        var from_time_hour_num = parseInt(from_time_hour);
        var from_time_min_num = parseInt(from_time_min);

        var to_time_hour_num = parseInt(to_time_hour);
        var to_time_min_num = parseInt(to_time_min);

        if(from_time_hour_num > 11 || from_time_hour_num < 0 ||
           from_time_min_num > 59 || from_time_min_num < 0 ||
           to_time_hour_num > 11 || to_time_hour_num < 0 ||
           to_time_min_num > 59 || to_time_min_num < 0){
            alert('Please don\'t change the values.');
            e.preventDefault();
            return false;
        }

        tr.children('td').css('display', 'none');

        tr.append('<td colspan="4" class="editor">' +
                  get_sched_editor(from_time_hour_num,
                                   from_time_min_num,
                                   from_time_m,
                                   to_time_hour_num,
                                   to_time_min_num,
                                   to_time_m) +
                  '</td>');
        e.preventDefault();
    });
});