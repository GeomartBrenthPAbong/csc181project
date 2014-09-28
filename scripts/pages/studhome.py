import scripts.global_variables as g
import scripts.classes.class_printable as p

def get_title():
	return 'Professor List'

def get_content():

	return "<h1>STUDENT PROFILE</h1><br>"


def get_page_template():
	return 'black_template'

def page_additions():
	rc_statement = "&nbsp;&nbsp;Find a professor and make appointments with them!"
	rc_content = """
					<div style="background-color:black; color:white; margin:20px; border-radius:15px; padding:20px;">
					<p>
					  <button id="btn-prev" type="button" class="btn btn-primary btn-xs">Previous</button>
					  <button id="btn-next" type="button" class="btn btn-primary btn-xs">Next</button>
					  <pre id="page">Page 1</pre>
					</p>
					<div id="proflist"></div>
					</div>
				"""
	g.g_header.getScriptAdder().add('proflist')
	g.g_header.getStyleAdder().add('studhome')
	g.g_locations.addToLocation('head_title', p.Printable("Home-" + g.g_user.getFirstName()))
	g.g_locations.addToLocation('right_content', p.Printable(rc_statement))
	g.g_locations.addToLocation('right_content', p.Printable(rc_content))

	content_list = g.g_locations.getContentsAtLocation('main_nav')
	if len(content_list) is 1:
		main_nav = content_list[0]
		main_nav.setAsActive('home')