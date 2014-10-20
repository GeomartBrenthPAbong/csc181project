
import scripts.global_variables as g
import scripts.classes.class_printable as p

def get_title():
	return 'Calendar of Appointments'

def get_content():
	return ''

def get_page_template():
	return 'black_template'

def page_additions():
	import scripts.functions as f

	if not f.user_logged_in():
		g.g_notification_title = 'Permission denied'
		g.g_notification_msg = 'You have no permission to access this page. ' \
							   'Please <a href="' +g.g_root_path + '/index.py' + '">sign in</a> first.'

		f.redirect(g.g_root_path + '/index.py?page=notification')
		return

	g.g_header.getScriptAdder().add('zabuto_calendar.min')
	g.g_header.getScriptAdder().add('profstudcalendar')

	g.g_header.getStyleAdder().add('zabuto_calendar.min')
	g.g_header.getStyleAdder().add('profstudcalendar')

	content_list = g.g_locations.getContentsAtLocation('main_nav')
	if content_list and len(content_list) is 1:
		main_nav = content_list[0]
		main_nav.setAsActive('appointments')

	g.g_locations.addToLocation('right_content', p.Printable('<div id="prof-stud-cal"></div>'))