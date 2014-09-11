import scripts.global_variables as g
import scripts.classes.class_printable as p

def get_title():
	return 'Login Page'

def get_content():
	return ''

def get_page_template():
	return 'clean_template'

def page_additions():
	#===== Scripts and Javascripts
	g.g_header.getStyleAdder().add('signin')

	#===== Contents Additions
	g.g_locations.addToLocation('main_content', p.Printable(g.g_login_form), 20)
	g.g_locations.addToLocation('title', p.Printable('Welcome to S.P.A.M'))
	g.g_locations.addToLocation('sub_title', p.Printable('Where Teachers and Students Collaborate Appointments'))

	#===== Defaults location addition
	g.g_locations.addToLocation('head_title', p.Printable(get_title()))



