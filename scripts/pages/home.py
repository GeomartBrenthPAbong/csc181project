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
	g.g_header.getScriptAdder().add('temp')

	# Location additions here

	#### head_title Location addition
	g.g_locations.addToLocation('head_title', p.Printable(get_title()))

	# Default changes here
	content_list = g.g_locations.getContentsAtLocation('main_nav')
	if not content_list is None and len(content_list) is 1:
		main_nav = content_list[0]
		main_nav.setAsActive('home')

	g.g_locations.addToLocation('after_content', p.Printable('<input type="submit" name="btn" value="Click me"/>'))
	g.g_locations.addToLocation('right_content', p.Printable('Home page here'))
	g.g_locations.addToLocation('after_content', p.Printable('<div id="sample-div">This a sample div</div>'))

