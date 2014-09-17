import scripts.global_variables as g
import scripts.classes.class_printable as p

def get_title():
	return 'Student Profile'
	
def get_content():
	html =	"""
			Some HTML code here...
			"""
	
	return html
	
	
def get_page_template():
	return 'black_template'
	
def page_additions():
	
	#stud_name = g.g_user.getFirstName() + " " + g.g_user.getLastName()
	stud_name = "Christopher Pacillos"
	g.g_locations.addToLocation('head_title', p.Printable("Home-" + stud_name))
	g.g_locations.addToLocation('after_content', p.Printable('gtsdfgsrgf'))
	g.g_header.getStyleAdder().add('signin')
	
	content_list = g.g_locations.getContentsAtLocation('main_nav')
	if len(content_list) is 1:
		main_nav = content_list[0]
		main_nav.setAsActive('home')