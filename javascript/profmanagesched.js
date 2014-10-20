function profmanagesched_main(){
    var data = {
        action: 'get_schedule_table'
    };

    ajaxify(data, function(response){
        if(response.status == 'SUCCESS')
            $('#sched-list').html(response.msg);
        else
            activate_modal(response.msg);
    });
}

jQuery(document).ready(function($){
    var g_current_sched;
    var g_modal_footer = $('#modal-footer');
    var g_right_content = $('.right-content');
    var g_editor = null;

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
            var schedule = '<tr id="' +response.data.id+ '">' +
                        '<td class="from-time">' + response.data.from_time + ' ' + '</td>' +
                        '<td class="to-time">' + response.data.to_time + ' ' + '</td>' +
                        '<td class="actions action-edit"><a href="#" class="edit">Edit</a></td>' +
                        '<td class="actions action-del"><a href="#" class="delete">Delete</a></td>' +
                    '</tr>';

            $('#' + response.data.day + ' table tbody').append(schedule);
        }
        else
            activate_modal('Request failed', response.msg);
    }

    //===== Event handlers
    g_right_content.on('click', 'input[name=btnAddSched]', function(e){
        e.preventDefault();
        e.stopPropagation();

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


        if(!valid_time_input2($('select[name=from-time-hour]').val(), $('select[name=from-time-min]').val(), $('select[name=from-time-m]').val(),
                              $('select[name=to-time-hour]').val(), $('select[name=to-time-min]').val(), $('select[name=to-time-m]').val())) {
            return false;
        }

        if($('select[name=from-time-m]').val() == 'pm')
           from_time += 1200;

        if($('select[name=to-time-m]').val() == 'pm')
           to_time += 1200;

        var day = $('select[name=day]').val();

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

        return false;
    });

    function valid_time_input(p_from_time_hour, p_from_time_min, p_from_time_m, p_to_time_hour, p_to_time_min, p_to_time_m){
        if(!$.isNumeric(p_from_time_hour) || !$.isNumeric(p_from_time_min) ||
           !$.isNumeric(p_to_time_hour) || !$.isNumeric(p_to_time_min)) {
            activate_modal('Error!', 'Please don\'t change the values.');
            return false;
        }
        if(!((p_from_time_m == 'am' || p_from_time_m == 'pm') && (p_to_time_m == 'am' || p_to_time_m == 'pm'))){
            activate_modal('Error!', 'Please don\'t change the values.');
            return false;
        }
        var p_from_time_hour_num = parseInt(p_from_time_hour);
        var p_from_time_min_num = parseInt(p_from_time_min);

        var p_to_time_hour_num = parseInt(p_to_time_hour);
        var p_to_time_min_num = parseInt(p_to_time_min);
        if(p_from_time_hour_num > 23 || p_from_time_hour_num < 0 ||
           p_from_time_min_num > 59 || p_from_time_min_num < 0 ||
           p_to_time_hour_num > 23 || p_to_time_hour_num < 0 ||
           p_to_time_min_num > 59 || p_to_time_min_num < 0){
            activate_modal('Error!', 'Please don\'t change the values.');
            return false;
        }
        return true;
    }

    function valid_time_input2(p_from_time_hour, p_from_time_min, p_from_time_m, p_to_time_hour, p_to_time_min, p_to_time_m){
        var from_time = (parseInt(p_from_time_hour) * 100) + (parseInt(p_from_time_min));
        var to_time = (parseInt(p_to_time_hour) * 100) + (parseInt(p_to_time_min));

        if(p_from_time_m == 'pm')
           from_time += 1200;

        if(p_to_time_m == 'pm')
           to_time += 1200;

        if((from_time < 700 || from_time > 2100) ||
            (to_time < 700 || from_time > 2100)){
            activate_modal('Error!', 'Time within the range [9:01pm, 6:59am] are not allowed.');
            return false;
        }

        if(get_time_difference(from_time, to_time) <= 0) {
            activate_modal('Error!', 'To time must be greater than the from time');
            return false;
        }

        if(get_time_difference(from_time, to_time) < 30) {
            activate_modal('Error!', 'The time range must be atleast 30 minutes');
            return false;
        }

        return true;
    }

    function reset_sched_editor(){
        $('#schedule-adder select[name="from-time-hour"]').selectmenu('refresh', true);
        $('#schedule-adder select[name="from-time-min"]').selectmenu('refresh', true);
        $('#schedule-adder select[name="from-time-m"]').selectmenu('refresh', true);

        $('#schedule-adder select[name="to-time-hour"]').selectmenu('refresh', true);
        $('#schedule-adder select[name="to-time-min"]').selectmenu('refresh', true);
        $('#schedule-adder select[name="to-time-m"]').selectmenu('refresh', true);
    }

    function get_sched_editor(p_from_hour, p_from_min, p_from_m, p_to_hour, p_to_min, p_to_m, p_day) {
        var schedule_editor = $('#schedule-adder form').clone(false);

        schedule_editor.find('tbody tr input[name="btnAddSched"]').remove();

        schedule_editor.find('td select[name="from-time-hour"] option').filter(function(){
            return parseInt($(this).val()) == parseInt(p_from_hour);
        }).attr('selected', true);

        schedule_editor.find('td select[name="from-time-min"] option').filter(function(){
            return parseInt($(this).val()) == parseInt(p_from_min);
        }).attr('selected', true);

        schedule_editor.find('td select[name="from-time-m"] option').filter(function(){
            return $(this).val() == p_from_m;
        }).attr('selected', true);

        schedule_editor.find('td select[name="to-time-hour"] option').filter(function(){
            return parseInt($(this).val()) == parseInt(p_to_hour);
        }).attr('selected', true);

        schedule_editor.find('td select[name="to-time-min"] option').filter(function(){
            return parseInt($(this).val()) == parseInt(p_to_min);
        }).attr('selected', true);

        schedule_editor.find('td select[name="to-time-m"] option').filter(function(){
            return $(this).val() == p_to_m;
        }).attr('selected', true);

        schedule_editor.find('td select[name="day"] option').filter(function(){
            return $(this).val() == p_day;
        }).attr('selected', true);

        editor = schedule_editor.html();

        return editor;
    }

    g_right_content.on('click', '#schedules td.action-edit a', function(e){
        e.preventDefault();
        e.stopPropagation();

        g_current_sched = $(this).closest('tr').attr('id');

        var from_time_str = $(this).parent().siblings('td.from-time').text().trim();
        var to_time_str = $(this).parent().siblings('td.to-time').text().trim();
        var day = $(this).closest('tr').parent().closest('tr').attr('id');

        var from_time_hour = from_time_str.substr(0, 2);
        var from_time_min = from_time_str.substr(3, 2);
        var from_time_m = from_time_str.slice(-2).toLowerCase();

        var to_time_hour = to_time_str.substr(0, 2);
        var to_time_min = to_time_str.substr(3, 2);
        var to_time_m = to_time_str.slice(-2).toLowerCase();

        if(!valid_time_input(from_time_hour, from_time_min, from_time_m, to_time_hour, to_time_min, to_time_m)){
            return false;
        }

        var editor = '<div id="editor">' +
                            get_sched_editor(from_time_hour,
                                   from_time_min,
                                   from_time_m,
                                   to_time_hour,
                                   to_time_min,
                                   to_time_m, day) +
                    '</div>';

        activate_modal('Edit your schedule',
                       editor,
                       '<input name="save-sched" type="text" value="Save" class="btn btn-lg btn-primary">' +
                       '<input name="cancel-action" type="text" value="Cancel" class="btn btn-lg btn-primary">');

        return false;
    });

    g_right_content.on('click', '#schedules td.action-del a', function(e){
        e.preventDefault();
        e.stopPropagation();

        g_current_sched = $(this).closest('tr').attr('id');

        activate_modal('Confirmation',
                       'Are you sure you want to delete this schedule?',
                       '<input name="del-sched" type="text" value="100% sure" class="btn btn-lg btn-primary">' +
                       '<input name="cancel-action" type="text" value="Cancel" class="btn btn-lg btn-primary">');

    });

    g_modal_footer.on('click', 'input[name="cancel-action"]', function(e){
        g_current_sched = null;
       close_modal();
       e.preventDefault();
    });

    function edit_sched_success_func(response){
        if(response.status == 'SUCCESS'){
            $('.right-content #schedules tr#' + response.data.id).remove();

            var schedule = '<tr id="' +response.data.id+ '">' +
                            '<td class="from-time">' + response.data.from_time + ' ' + '</td>' +
                            '<td class="to-time">' + response.data.to_time + ' ' + '</td>' +
                            '<td class="actions action-edit"><a href="#" class="edit">Edit</a></td>' +
                            '<td class="actions action-del"><a href="#" class="delete">Delete</a></td>' +
                            '</tr>';

            $('tr#' + response.data.day + ' table tbody').append(schedule);
            close_modal();
        }
        else
            activate_modal('Error!', response.msg);
        reset_sched_editor();
    }

    g_modal_footer.on('click', 'input[name="save-sched"]', function(e){
        e.preventDefault();
        e.stopPropagation();

        var from_time_hour = $('#modal-body #editor select[name="from-time-hour"]').val();
        var from_time_min = $('#modal-body #editor select[name="from-time-min"]').val();
        var from_time_m = $('#modal-body #editor select[name="from-time-m"]').val();

        var to_time_hour = $('#modal-body #editor select[name="to-time-hour"]').val();
        var to_time_min = $('#modal-body #editor select[name="to-time-min"]').val();
        var to_time_m = $('#modal-body #editor select[name="to-time-m"]').val();

        var day = $('#modal-body #editor select[name="day"]').val();

        if(!valid_time_input(from_time_hour, from_time_min, from_time_m, to_time_hour, to_time_min, to_time_m)){
            return false;
        }

        if(!valid_time_input2(from_time_hour, from_time_min, from_time_m, to_time_hour, to_time_min, to_time_m)){
            return false;
        }

        if(from_time_m == 'pm')
           from_time_hour = parseInt(from_time_hour) + 12;

        if(to_time_m == 'pm')
           to_time_hour = parseInt(to_time_hour) + 12;

        var data = {
          action: 'edit_schedule',
          from_time_hour: from_time_hour,
          from_time_min: from_time_min,
          to_time_hour: to_time_hour,
          to_time_min: to_time_min,
          day: day,
          id: g_current_sched
        };

        ajaxify(data, edit_sched_success_func);

        return false;
    });


    function del_sched_success_func(response){
        if(response.status == 'SUCCESS'){
            $('.right-content #schedules tr#' + response.id).remove();
            close_modal();
        }
        else
            activate_modal('Error!', response.msg);
    }

    g_modal_footer.on('click', 'input[name="del-sched"]', function(e){
        e.preventDefault();
        e.stopPropagation();

        var data = {
            action: 'delete_schedule',
            prof_sched_id: g_current_sched
        }

        ajaxify(data, del_sched_success_func);
        return false;
    });

    profmanagesched_main();
});