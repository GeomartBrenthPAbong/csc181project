import scripts.global_variables as g
import scripts.classes.class_printable as p

def get_title():
	return 'Professor Profile'

def get_content():
	return ''

def get_page_template():
	return 'black_template'

def page_additions():
	# Styles and Scripts additions here

	# Location additions here

	#### head_title Location addition
	#prof_name = g.g_user.getFirstName() + " " + g.g_user.getLastName()
	#g.g_locations.addToLocation('head_title', p.Printable(prof_name))
	
	g.g_locations.addToLocation('head_title', p.Printable(g.g_content.getTitle()))

	# Default changes here
	content_list = g.g_locations.getContentsAtLocation('main_nav')
	if len(content_list) is 1:
		main_nav = content_list[0]
		main_nav.setAsActive('home')
		
	g.g_header.getStyleAdder().add('profile')
	html = """ 	<div id="nav">
					<img src="#../spam/picture/profilepics/" alt="PIC" width="290px" height="290px">
				</div>
				<div id="section">
					<h4>Position:</h4>
					<h4>Degree:</h4>
					<h4>Age:</h4>
					<h4>Birthdate:</h4>
					
				</div>
			"""

	
	g.g_locations.addToLocation('after_content', p.Printable(html))



