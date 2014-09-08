import global_variables
import classes.class_header
import classes.class_content
import classes.class_footer
import types
#import recipe

##===== Admin functions here

## Starts a session for saving data in the server
#def session_start():
#	global_variables.g_session = recipe.SESSION
#	global_variables.g_session.start()

## Destroys the session variable and sets it to None
#def session_destroy():
#	global_variables.g_session.destroy()
#	global_variables.g_session = None

## Returns true if the user is logged in otherwise, returns false
#def is_user_logged_in():
#	return global_variables.g_session.isset( 'logged_in' )

## Initialize global variables here
def pre_processing():
	global_variables.g_style_adder = classes.class_style_adder.StyleAdder()
	global_variables.g_header = classes.class_header.Header()
	global_variables.g_content = classes.class_content.Content()
	global_variables.g_content.extractPage(global_variables.g_page)
	global_variables.g_footer = classes.class_footer.Footer()

## Add scripts here
def post_processing():
	global_variables.g_header.getStyleAdder().add('styles')

	global_variables.g_header.getScriptAdder().add('jquery-2.1.1.min')
	global_variables.g_header.getScriptAdder().add('general')

def function_exists( p_function_name ):
		try:
			ret = type( eval( str( p_function_name ) ) )
			return ret in ( types.FunctionType, types.BuiltinFunctionType )
		except NameError:
			return False

def page_validation( p_page_name ):
	import os
	try:
		if os.path.isfile( global_variables.g_main_path + '/scripts/pages/' + p_page_name + '.py' ):
			global_variables.g_page = p_page_name
		else:
			raise IOError()
	except IOError:
		global_variables.g_page = 'notification'
		global_variables.g_notification_title = '404 Not Found'
		global_variables.g_notification_msg = 'This page does not exists.'

##===== AJAX callable functions here

## Used for logging in
