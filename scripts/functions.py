import global_variables
import classes.class_header
import classes.class_content
import classes.class_footer
import classes.class_locations
import types
##===== Admin functions here

## Returns true if the user is logged in otherwise, returns false
def user_logged_in():
	return True

## Initialize global variables here
def pre_processing():
	global_variables.g_header = classes.class_header.Header()
	global_variables.g_content = classes.class_content.Content()
	global_variables.g_content.setPage(global_variables.g_page_name)
	global_variables.g_footer = classes.class_footer.Footer()
	global_variables.g_locations = classes.class_locations.Locations()

def process_page():
	from mod_python import apache
	import classes.class_dosql as sql

	page = apache.import_module(global_variables.g_page_name, path=[global_variables.g_main_path + '/scripts/pages/'])
	page.page_additions()
	global_variables.g_content.setTitle(page.get_title())
	global_variables.g_content.setContent(page.get_content())
	global_variables.g_content.setPageTemplate(page.get_page_template())
	#global_variables.g_sql = sql.doSql()
	global_variables.g_page = page

def post_processing():
	from mod_python import apache
	import global_variables as g

	page_template = apache.import_module(g.g_page.get_page_template(), path=[g.g_main_path + '/scripts/page_templates/'])
	g.g_content.setContent(page_template.generate_page())


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
		global_variables.g_page_name = 'notification'
		global_variables.g_notification_title = '404 Not Found'
		global_variables.g_notification_msg = 'This page does not exists.'

def setup_cookies(p_cookie_data):
	import Cookie

	cookie = Cookie.SimpleCookie()
	cookie['logged_in'] = p_cookie_data

def user_exists(p_user_id):
	return global_variables.g_sql.execqry('checkUserExistence(' + p_user_id + ')') != 'None'

def appointment_exists(p_professor_id, p_student_id):
	return global_variables.g_sql.execqry('getApptPerStudProfId(' + p_professor_id + ', ' + p_student_id + ')') != 'None'

def schedule_time_exists(p_from_time, p_to_time):
	return not global_variables.g_sql.execqry("SELECT * FROM checkSchedExistencePerTimeRange('" + p_from_time + "', '" + p_to_time + "')", False)

def schedule_exists(p_schedule_id):
	return global_variables.g_sql.execqry("SELECT * FROM checkSchedExistencePerID('" + p_schedule_id + "')", False) != 'None'

def is_time_format(p_time):
	return True

def is_date_format(p_date):
	import datetime
	try:
		datetime.datetime.strptime(p_date, '%m/%d/%Y')
		return True
	except ValueError:
		return False

def is_day(p_day):
	days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

	for day in days:
		if p_day == day:
			return True
	return False

def generate_numbers(p_min, p_max):
	numbers = []
	for number in range(p_min, p_max):
		numbers.append(
			{
				'value': str(number),
				'label': str("%02d" % number)
			}
		)
	return numbers

def gen_prof_list(req):
    import classes.class_dosql as sqlDriver

    offset = req.form.getfirst('offset')
    name = req.form.getfirst('name')

    if offset is None:
        offset = '0'

    if name is None:
        query = "SELECT * FROM getUsersLimitOffset('Professor',"
        query += "'" + req.form.getfirst('limit')
        query += "','" + offset + "')"
    else:
        query = "SELECT * FROM getUsersLimitOffsetNameSearch('Professor',"
        query += "'" + req.form.getfirst('name')
        query += "','" + req.form.getfirst('limit')
        query += "','" + offset + "')"


    f = sqlDriver.doSql()
    return f.execqry(query, False)