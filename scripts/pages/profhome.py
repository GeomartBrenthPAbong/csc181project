import scripts.global_variables as g
import scripts.classes.class_printable as p

def get_title():
	return 'Professor Profile'

def get_content():
	return 'Hey'

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

	# Styles and Scripts additions here

	# Location additions here

	#### head_title Location addition
	#prof_name = g.g_user.getFirstName() + " " + g.g_user.getLastName()
	#g.g_locations.addToLocation('head_title', p.Printable(prof_name))
	
	g.g_locations.addToLocation('head_title', p.Printable(get_title()))

	#Default changes here
	content_list = g.g_locations.getContentsAtLocation('main_nav')
	if not content_list is None and len(content_list) is 1:
		main_nav = content_list[0]
		main_nav.setAsActive('home')

	g.g_header.getStyleAdder().add('profile')

	profdetails = 'USER NAME: ' + g.g_user.getFirstName() + ' ' + g.g_user.getLastName()

	g.g_locations.addToLocation('right_content', p.Printable(profdetails))


