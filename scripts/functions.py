import global_variables
import classes.class_header
import classes.class_content
import classes.class_footer
import classes.class_locations
import types
##===== Admin functions here

## Returns true if the user is logged in otherwise, returns false
def user_logged_in():
	return global_variables.g_user is not None

def create_user():
	import mod_python.Cookie as Cookie

	try:
		c = Cookie.get_cookies(global_variables.g_req, Cookie.MarshalCookie, secret='popcorn')
		if not 'session_id' in c:
			return None

		session_id = c["session_id"].value
	except (Cookie.CookieError, KeyError, Exception):
		return None

	import classes.class_user_factory as user_factory
	import exceptions.e_notregistered as e_notregistered
	import scripts.classes.class_dosql as sql

	dosql = sql.doSql()

	try:
		((username,),) = dosql.execqry("SELECT * FROM getUser('" + str(session_id) + "')", False)
		return user_factory.UserFactory().createUserFromID(username)
	except (e_notregistered.ENotRegistered, Exception):
		return None

def authenticate_user(p_username, p_password):
	((status,),) = global_variables.sql.execqry("SELECT * FROM userAuthentication('" + p_username + "', '" + p_password + "'")
	return status

def redirect(p_url):
	from mod_python import util
	import scripts.global_variables as g

	util.redirect(g.g_req, p_url)

def log_user_in(p_username):
	from mod_python import Cookie
	import time
	import uuid

	session_id = None

	while True:
		session_id = uuid.uuid4()

		((is_unique_session,),) = global_variables.g_sql.execqry("SELECT * FROM saveSessionID('" + str(session_id) + "', '" + p_username + "')", True)
		if is_unique_session:
			break

	c = Cookie.Cookie('session_id', session_id)
	c.expires = time.time() + 432000.0
	Cookie.add_cookie(global_variables.g_req, c)

def log_user_out():
	import mod_python.Cookie as Cookie

	try:
		c = Cookie.get_cookies(global_variables.g_req, Cookie.MarshalCookie, secret='popcorn')
		if not 'session_id' in c:
			return False

		session_id = c["session_id"].value
		global_variables.g_sql.execqry("SELECT * FROM deleteSession('" + session_id + "')", True)
		return True
	except (Cookie.CookieError, KeyError, Exception):
		return False


## Initialize global variables here
def pre_processing():
	import classes.class_dosql as sql

	global_variables.g_header = classes.class_header.Header()
	global_variables.g_content = classes.class_content.Content()
	global_variables.g_content.setPage(global_variables.g_page_name)
	global_variables.g_footer = classes.class_footer.Footer()
	global_variables.g_locations = classes.class_locations.Locations()
	global_variables.g_sql = sql.doSql()

def process_page():
	from mod_python import apache

	page = apache.import_module(global_variables.g_page_name, path=[global_variables.g_main_path + '/scripts/pages/'])
	page.page_additions()
	global_variables.g_content.setTitle(page.get_title())
	global_variables.g_content.setContent(page.get_content())
	global_variables.g_content.setPageTemplate(page.get_page_template())

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
		global_variables.g_notification_msg = 'This page does not exist.'

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



def gen_appt_list(p_offset, p_status, p_limit):
	import scripts.classes.class_dosql as sql
	import scripts.classes.class_appointment as appt
	import scripts.exceptions.e_notregistered as en

	global_variables.g_sql = sql.doSql()

	result = global_variables.g_user.getAppointments(p_status, p_limit, p_offset)

	if is_none_list(result):
		raise Exception('No results found.')

	appointments = []

	for (res,) in result:
		try:
			details = {}
			app = appt.Appointment().dbExtract(res)
			prof = app.getProfessor()
			stud = app.getStudent()
			sched = app.getProfSchedule()

			details['curr_user_type'] = global_variables.g_user.getType()
			details['appt_id'] = res
			details['prof_name'] = prof.getFirstName() + ' ' + prof.getLastName()
			details['stud_name'] = stud.getFirstName() + ' ' + stud.getLastName()
			details['sched_from_time'] = h24_to_h12(sched.getFromTime().strftime('%H:%M'))
			details['sched_to_time'] = h24_to_h12(sched.getToTime().strftime('%H:%M'))
			details['app_date'] = str(app.getAppointmentDate())
			details['app_msg'] = app.getAppointmentMsg()
			appointments.append(details)
		except en.ENotRegistered:
			continue
		except Exception:
			continue

	return appointments

def gen_appt_details(p_appointment_id):
	import scripts.classes.class_appointment as appt

	app = appt.Appointment().dbExtract(p_appointment_id)

	prof_name = app.getProfessor().getFirstName() + ' ' + app.getProfessor().getLastName()
	prof_id = app.getProfessor().getID()
	stud_name = app.getStudent().getFirstName() + ' ' + app.getStudent().getLastName()
	stud_id = app.getStudent().getID()
	stud_course = app.getStudent().getCourse()
	sched_from_time = h24_to_h12(app.getProfSchedule().getFromTime().strftime('%H:%M'))
	sched_to_time = h24_to_h12(app.getProfSchedule().getToTime().strftime('%H:%M'))
	app_date = str(app.getAppointmentDate())
	app_msg = app.getAppointmentMsg()
	app_stat = app.getStatus()

	app.setStateViewed(True)
	app.changeStateViewed()

	return [(prof_name, stud_name,
			 stud_id, stud_course,
			 sched_from_time,
			 sched_to_time, app_date,
			 app_msg, app_stat,
			 global_variables.g_user.getType(), prof_id)]

def change_status(p_appointment_id, p_new_status):
	import scripts.classes.class_appointment as app

	appointment = app.Appointment().dbExtract(p_appointment_id)
	appointment.setStatus(p_new_status)
	appointment.changeStatus()
	appointment.setStateViewed(True)
	appointment.changeStateViewed()

	stud = appointment.getStudent()

	return {'stud_name': stud.getFirstName() + ' ' + stud.getLastName()}


def gen_prof_details(req):
	import scripts.classes.class_user_factory as uf

	id = req.form.getfirst('data')
	users = uf.UserFactory.createUserFromID(id)
	prof_id = users.getID()
	college = users.getCollege()
	department = users.getDepartment()
	email = users.getEmailAddress()
	address = users.getAddress()
	phone_number = users.getPhoneNumber()
	first_name = users.getFirstName()
	last_name = users.getLastName()
	return [(prof_id,college,department,email,address,phone_number,first_name,last_name)]

def cancel_appt(req):
	import scripts.classes.class_dosql as sqlDriver

	appt_id = req.form.getfirst('appt_id')
	query = "SELECT * FROM deleteAppt("
	query += appt_id + ")"

	f = sqlDriver.doSql()
	return f.execqry(query,True)

def gen_prof_sched(req):
	import scripts.classes.class_dosql as sqlDriver

	id = req.form.getfirst('id')
	query = "SELECT * FROM getSchedDetailsFromProfSched('"
	query += id + "')"


	f = sqlDriver.doSql()
	results = f.execqry(query, False)

	list = []

	for result in results:
		data = []
		for datum in result:
			data.append(str(datum))
		list.append(data)
	return list
