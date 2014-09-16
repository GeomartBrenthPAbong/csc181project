import scripts.global_variables as g
import scripts.classes.class_printable as p
import scripts.forms.form_login as login_form

def get_title():
	return 'Login Page'

def get_content():
	return ''

def get_page_template():
	return 'clean_template'

def page_additions():
	#===== Styles and Javascripts
	g.g_header.getStyleAdder().add('signin')

	#===== Contents Additions
	g.g_locations.addToLocation('main_content', p.Printable(login_form.get_form()))
	g.g_locations.addToLocation('title', p.Printable('Welcome to S.P.A.M'))
	g.g_locations.addToLocation('sub_title', p.Printable('Where Teachers and Students Collaborate Appointments'))

	#===== Defaults location addition
	g.g_locations.addToLocation('head_title', p.Printable(get_title()))



