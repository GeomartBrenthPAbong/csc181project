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
	import scripts.functions as f

	if f.user_logged_in():
		if g.g_user.getType() == 'Student':
			f.redirect(g.g_root_path + '/index.py?page=studhome')
		else:
			f.redirect(g.g_root_path + '/index.py?page=profmanagesched')

	#===== Styles and Javascripts
	g.g_header.getStyleAdder().add('signin')
	g.g_header.getScriptAdder().add('login')

	#===== Contents Additions
	g.g_locations.addToLocation('main_content', login_form.get_form())
	g.g_locations.addToLocation('title', p.Printable('Welcome to S.P.A.M'))
	g.g_locations.addToLocation('sub_title', p.Printable('Where Teachers and Students Collaborate Appointments'))

	#===== Defaults location addition
	g.g_locations.addToLocation('head_title', p.Printable(get_title()))



