import scripts.global_variables as g
import scripts.classes.class_printable as p

def get_title():
	return 'Student Profile'
	
def get_content():
	html =	"""
			<div id = "picture">
				<img src="../spam/picture/user/student/2009-0731.png" alt="No picture found." style="width:290px;height:290px">
			</div>
			"""
	
	return html
	
	
def get_page_template():
	return 'black_template'
	
def page_additions():
	g.g_header.getStyleAdder().add('profile')
	#stud_name = g.g_user.getFirstName() + " " + g.g_user.getLastName()
	stud_name = "Christopher Pacillos"
	
	details_html =	"""					
					<div id="details">
						<h1>Christopher Clint Pacillos</h1>
					<p>
						Bachelor of Science in Compputer Engineering
					</p>
					<p>
						<br>Some other details here...
					</p>
					</div>
					"""
	g.g_locations.addToLocation('head_title', p.Printable("Home-" + stud_name))
	g.g_locations.addToLocation('after_content', p.Printable(details_html))
	g.g_locations.addToLocation('footer', p.Printable("These are some footer content."))
	
	content_list = g.g_locations.getContentsAtLocation('main_nav')
	if len(content_list) is 1:
		main_nav = content_list[0]
		main_nav.setAsActive('home')