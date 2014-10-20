import scripts.global_variables as g
import scripts.classes.class_printable as p
import scripts.forms.form_add_sched as form
import scripts.classes.class_schedule as sched
import scripts.classes.class_professor as prof
import scripts.functions as f

def get_title():
	return 'Manage Schedules'

def get_content():
	return ''

def get_page_template():
	return 'black_template'

def page_additions():
	if not f.user_logged_in() or g.g_user.getType() != 'Professor':
		if g.g_ajax_req:
			return

		g.g_notification_title = 'Permission denied'
		g.g_notification_msg = 'You have no permission to access this page. ' \
							   'Please <a href="' +g.g_root_path + '/index.py' + '">sign in</a> first.'

		f.redirect(g.g_root_path + '/index.py?page=notification')
		return

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

	schedule_div = """<div style="margin-left:8px; margin-top:20px;" id="schedules" class="panel panel-default">
							<div class="panel-heading"><b>Schedules</b></div>
							<div class="panel-body">
					"""

	schedule_div += """<table class="table table-hover">
								<thead>
									<tr>
										<th class="day">Day</th>
										<th class="from-time">From Time</th>
										<th class="to-time">To Time</th>
										<th>Action</th>
									</tr>
								</thead>
							<tbody id="sched-list" data-link="row" class="rowlink">
					"""


	schedule_div += '</tbody></table>'

	schedule_div += '</div></div>'
	g.g_locations.addToLocation('right_content', p.Printable(schedule_div))


