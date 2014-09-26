import scripts.global_variables as g
import scripts.classes.class_printable as p
import scripts.classes.class_student as s
import scripts.functions as f

def get_title():
	return 'Student Profile'
	
def get_content():
	return ""
	
	
def get_page_template():
	return 'black_template'
	
def page_additions():
	
	#if not f.user_logged_in():
		#pass
		#use a redirect function
	stud_name = g.g_user.getFirstName() + " " + g.g_user.getLastName()
		
	g.g_locations.addToLocation('head_title', p.Printable("Home-" + stud_name))
	g.g_locations.addToLocation('right_content', p.Printable("Search here."))	
	
	content_list = g.g_locations.getContentsAtLocation('main_nav')
	if len(content_list) is 1:
		main_nav = content_list[0]
		main_nav.setAsActive('home')