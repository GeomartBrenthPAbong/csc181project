import scripts.global_variables as g
import scripts.classes.class_printable as p

def get_title():
	return 'Home'

def get_content():
	return 'This is the homepage.'

def get_page_template():
	return 'black_template'

def page_additions():
	# Styles and Scripts additions here

	# Location additions here

	#### head_title Location addition
	g.g_locations.addToLocation('head_title', p.Printable(g.g_content.getTitle()))

	# Default changes here
	content_list = g.g_locations.getContentsAtLocation('main_nav')
	if len(content_list) is 1:
		main_nav = content_list[0]
		main_nav.setAsActive('home')


