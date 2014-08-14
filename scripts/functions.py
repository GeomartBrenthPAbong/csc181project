
import global_variables
import classes.class_header
import classes.class_content
import classes.class_footer

# initialize global variables here
def pre_processing():
	global_variables.g_style_adder = classes.class_style_adder.StyleAdder()
	global_variables.g_header = classes.class_header.Header()
	global_variables.g_content = classes.class_content.Content()
	global_variables.g_content.extractPage(global_variables.g_page)
	global_variables.g_footer = classes.class_footer.Footer()

def post_processing():
	global_variables.g_header.getStyleAdder().add('styles')

	global_variables.g_header.getScriptAdder().add('jquery-2.1.1.min')
	global_variables.g_header.getScriptAdder().add('general')