import scripts.global_variables as g
import scripts.classes.class_printable as p

def get_title():
	return 'Request Appointment'

def get_content():
	html =	"""
	   <div id="sprofile"><h1 style="font-weight: bold;">STUDENT</h1></div>
			"""

	return html

def get_page_template():
	return 'black_template'

def page_additions():
	rc_statement = """<button id="btn-modal" type="button" class="btn btn-primary btn-large">Try!</button>"""
	g.g_header.getScriptAdder().add('general')
	g.g_header.getScriptAdder().add('stud_request_appointment')
	g.g_locations.addToLocation('right_content', p.Printable(rc_statement))
