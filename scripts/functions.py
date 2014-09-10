import global_variables
import classes.class_header
import classes.class_content
import classes.class_footer
import classes.class_locations
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
def is_user_logged_in():
	return True
#	return global_variables.g_session.isset( 'logged_in' )

## Initialize global variables here
def pre_processing():
	global_variables.g_style_adder = classes.class_style_adder.StyleAdder()
	global_variables.g_header = classes.class_header.Header()
	global_variables.g_content = classes.class_content.Content()
	global_variables.g_content.setPage(global_variables.g_page_name)
	global_variables.g_footer = classes.class_footer.Footer()
	global_variables.g_locations = classes.class_locations.Locations()

def process_page():
	from mod_python import apache

	page = apache.import_module(global_variables.g_page_name, path=[global_variables.g_main_path + '/scripts/pages/'])
	global_variables.g_content.setTitle(page.get_title())
	global_variables.g_content.setContent(page.get_content())
	global_variables.g_content.setPageTemplate(page.get_page_template())
	page.page_additions()

	page_template = apache.import_module(page.get_page_template(), path=[global_variables.g_main_path + '/scripts/page_templates/'])
	global_variables.g_content.setContent(page_template.generate_page())

def function_exists(p_function_name):
	try:
		ret = type( eval( str( p_function_name ) ) )
		return ret in ( types.FunctionType, types.BuiltinFunctionType )
	except NameError:
		return False

def module_exists(p_module_name, p_rel_main_path):
	import os
	try:
		return os.path.isfile( global_variables.g_main_path + p_rel_main_path + p_module_name + '.py' )
	except IOError:
		return False

def page_validation(p_page_name):
	if module_exists( p_page_name, '/scripts/pages/' ):
		global_variables.g_page_name = p_page_name
	else:
		global_variables.g_page = 'notification'
		global_variables.g_notification_title = '404 Not Found'
		global_variables.g_notification_msg = 'This page does not exists.'

##===== AJAX callable functions here

## Used for logging in

def spam_in_test_ajax():
	import cgi
	import scripts.third_party_modules.simplejson.simplejson as json

	values = cgi.FieldStorage
	response = dict

	response['status'] = 'SUCCESS'
	response['msg'] = 'You sent: ' + values['value']
	return json.dumps( response )