var g_psc_appointments;

function show_mini_appointment_details(p_cal_id){
    var cal = $('#' + p_cal_id);

    if(!cal.data('hasEvent'))
        return;

    activate_modal('Pending/Confirmed appointments on ' + cal.data('date'),
                   $('#' + p_cal_id + '_day').data('event'));
}

function psc_onload(){
    var date = new Date();
    var last_day = new Date(date.getFullYear(), date.getMonth() + 1, 0);

    var fdate_str = date.getFullYear() + '-' + (date.getMonth() + 1) + '-1';
    var ldate_str = date.getFullYear()  + '-' + (date.getMonth() + 1) + '-' + last_day.getDate();

    $('#prof-stud-cal').zabuto_calendar({
                            cell_border: true,
                            today: true,
                            show_previous: false,
                            show_next: 2,
                            nav_icon: { prev: '<i class="fa fa-chevron-circle-left">&lt;&lt;</i>',
                                        next: '<i class="fa fa-chevron-circle-right">&gt;&gt;</i>' },
                            action: function () {
                                return show_mini_appointment_details(this.id); },
                            ajax: {
                              url: 'http://localhost/spam/ajax.py?action=gen_app_list_per_time&from_date=' + fdate_str + '&to_date=' + ldate_str,
                              modal: true }
                       });
}

function profstudcalendar_main(){
    psc_onload();
}

jQuery(document).ready(function(){
    profstudcalendar_main();
});



