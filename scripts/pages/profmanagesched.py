import scripts.global_variables as g
import scripts.classes.class_printable as p
import scripts.forms.form_add_sched as form
import scripts.classes.class_schedule as sched
import scripts.classes.class_professor as prof

def get_title():
	return 'Manage Schedules'

def get_content():
	return ''

def get_page_template():
	return 'black_template'

def page_additions():
	# Styles and Scripts additions here
	g.g_header.getStyleAdder().add('profmanagesched')
	g.g_header.getScriptAdder().add('sprintf')
	g.g_header.getScriptAdder().add('profmanagesched')

	# Location additions here

	#### head_title Location addition
	#prof_name = g.g_user.getFirstName() + " " + g.g_user.getLastName()
	#g.g_locations.addToLocation('head_title', p.Printable(prof_name))

	g.g_locations.addToLocation('head_title', p.Printable(g.g_content.getTitle()))

	# Default changes here
	content_list = g.g_locations.getContentsAtLocation('main_nav')
	if not content_list is None and len(content_list) is 1:
		main_nav = content_list[0]
		main_nav.addMenuItem('profmanagesched', 'Manage Schedules', g.g_root_path + '/index.py?page=profmanagesched')
		main_nav.setAsActive('profmanagesched')

	## right_content location additions
	g.g_locations.addToLocation('right_content', p.Printable('<div id="schedule-adder"><h4 class="sub-title">Schedule Adder</h4>'), 1)
	g.g_locations.addToLocation('right_content', form.get_form(), 2)
	g.g_locations.addToLocation('right_content', p.Printable('</div>'), 3)

	schedule_div = '<div id="schedules"><h4>Schedules</h4>'
	if not g.g_user is None and isinstance(g.g_user, prof.Professor):
		schedules = g.g_user.getSchedules()

		if len(schedules) > 0:
			schedule_div += """<table>
									<tr>
										<td>From Time</td>
										<td>To Time</td>
										<td>Day</td>
										<td colspan="2">Action</td>
									</tr>
									<tr>"""
			for sched_id in schedules:
				schedule = sched.Schedule().dbExtract(sched_id)

				schedule_div += '<td class="from-time">' + schedule.getFromTime() + '</td>'
				schedule_div += '<td class="to-time">' + schedule.getToTime() + '</td>'

				schedule_div += '<td class="day">' + schedule.getScheduleDay(schedule) + '</td>'
				schedule_div += '<td class="actions"><a href="#" class="edit">Edit</a></td>'
				schedule_div += '<td class="actions"><a href="#" class="delete">Delete</a></td>'

			schedule_div += '</tr></table>'
		else:
			schedule_div += '<p class="warn">No schedules.</p>'
	else:
		schedule_div += '<p class="warn">No schedules.</p>'
	schedule_div += '</div>'
	g.g_locations.addToLocation('right_content', p.Printable(schedule_div))


