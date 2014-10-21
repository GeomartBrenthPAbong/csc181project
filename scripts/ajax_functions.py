import global_variables as g
import third_party_modules.simplejson.simplejson as json

def spam_out_login():
	import scripts.classes.class_user_factory as user_factory
	import scripts.exceptions.e_notregistered as e_notregistered
	import scripts.classes.class_dosql as sql

	g.g_sql = sql.doSql()

	username = g.g_req.form.getfirst('username')
	password = g.g_req.form.getfirst('password')

	try:
		g.g_user = user_factory.UserFactory().createUserFromUname(username, password)
	except e_notregistered.ENotRegistered, e:
		return json.dumps({'status': 'FAILED',
						   'msg': e.getMessage()})

	import scripts.functions as f

	f.log_user_in(username)

	if g.g_user.getType() == 'student':
		redirect_url = g.g_root_path + '/index.py?page=studhome'
	else:
		redirect_url = g.g_root_path + '/index.py?page=profhome'

	return json.dumps({'status': 'SUCCESS',
					   'redirect_url': redirect_url})

def spam_in_logout():
	import functions as f
	import classes.class_dosql as sql

	g.g_sql = sql.doSql()

	if f.log_user_out():
		return json.dumps({'status': 'SUCCESS',
							'redirect_url': g.g_root_path + '/index.py?page=login_page'})
	return json.dumps({'status': 'FAILED',
					   'msg': 'Sorry, can\'t log you out right now. Please try again later.'})

def spam_in_add_schedule():
	import scripts.classes.class_user_factory as uf
	import scripts.classes.class_schedule as s
	import scripts.exceptions.e_spam as espam
	import scripts.classes.class_dosql as sql

	from_time = g.g_req.form.getfirst('from_time')
	to_time = g.g_req.form.getfirst('to_time')
	day = g.g_req.form.getfirst('day')
	msg = ''
	data = {'from_time': from_time,
			'to_time': to_time,
			'day': day}
	g.g_sql = sql.doSql()

	try:
		user = uf.UserFactory().createUserFromID('09-040')
		schedule = s.Schedule().createObject((from_time, to_time))
		schedule.dbStore()
		data['id'] = user.addSchedule(schedule, day)
	except espam.ESpam, spam:
		msg = spam.getMessage()
	except Exception, e:
		msg = e.message

	return json.dumps({'status': 'SUCCESS',
						'msg': msg,
						'data': data})

def spam_in_get_page_content():
	import functions as f

	g.g_page_name = g.g_req.form.getfirst('page_name')
	page_locations = json.loads(g.g_req.form.getfirst('page_location'))

	f.page_validation(g.g_page_name)
	if g.g_page_name == 'notification':
		return json.dumps({'status': 'FAILED', 'data': {
			'title': g.g_notification_title,
			'right_content': g.g_notification_msg
		}})

	f.process_page()

	locations = {}
	for location in page_locations:
		if location == 'main_content':
			locations[location] = g.g_content.getContent()
		elif location == 'title':
			locations[location] = g.g_content.getTitle()
		else:
			locations[location] = g.g_locations.printContentsAtLocation(location)

	return json.dumps({'status': 'SUCCESS', 'data': locations})


def spam_in_gen_prof_list():
	import functions as f

	return json.dumps({'status': 'SUCCESS', 'msg': f.gen_prof_list(g.g_req) })

def spam_in_gen_appt_list():
	import functions as f

	offset = g.g_req.form.getfirst('offset')
	stat = g.g_req.form.getfirst('stat')
	limit = g.g_req.form.getfirst('limit')

	if offset is None:
		offset = 0
	if limit is None:
		limit = 'ALL'

	try:
		return json.dumps({'status': 'SUCCESS', 'msg': f.gen_appt_list(offset, stat, limit)})
	except Exception, e:
		return json.dumps({'status': 'FAILED', 'msg': str(e)})

def spam_in_gen_appt_details():
	import functions as f
	import scripts.exceptions.e_notregistered as en

	appointment_id = g.g_req.form.getfirst('appt_id')

	try:
		return json.dumps({'status': 'SUCCESS', 'msg': f.gen_appt_details(appointment_id)})
	except en.ENotRegistered:
		return json.dumps({'status': 'FAILED', 'msg': 'Appointment does not exist.'})
	except Exception, e:
		return json.dumps({'status': 'FAILED', 'msg': str(e)})

def spam_in_change_status():
	import functions as f
	import scripts.exceptions.e_notregistered as en

	appointment_id = g.g_req.form.getfirst('appt_id')
	new_status = g.g_req.form.getfirst('stat')

	try:
		return json.dumps({'status': 'SUCCESS', 'msg': f.change_status(appointment_id, new_status)})
	except en.ENotRegistered:
		return json.dumps({'status': 'FAILED', 'msg': 'Appointment does not exists'})
	except Exception, e:
		return json.dumps({'status': 'FAILED', 'msg': str(e)})

def spam_in_gen_prof_details():
	import functions as f
	import scripts.classes.class_dosql as sql

	g.g_sql = sql.doSql()
	return json.dumps({'status': 'SUCCESS', 'msg': f.gen_prof_details(g.g_req)})

def spam_in_cancel_appt():
	import functions as f
	return json.dumps({'status': 'SUCCESS', 'msg': f.cancel_appt(g.g_req)})

def spam_in_gen_prof_sched():
	import functions as f
	import scripts.exceptions.e_notregistered as en

	prof_id = g.g_req.form.getfirst('id')

	try:
		return json.dumps({'status': 'SUCCESS', 'msg': f.gen_prof_sched(prof_id)})
	except en.ENotRegistered:
		return json.dumps({'status': 'FAILED', 'msg': 'Professor does not exists'})
	except Exception, e:
		return json.dumps({'status': 'FAILED', 'msg': str(e)})

def spam_in_gen_app_list_per_time():
	import scripts.classes.class_dosql as sql
	import scripts.functions as f

	g.g_sql = sql.doSql()

	from_date = g.g_req.form.getfirst('from_date')
	to_date = g.g_req.form.getfirst('to_date')

	try:
		appointment_date = g.g_user.getAppointmentsPerDate(from_date, to_date)

		grouped_app = {}
		for (app_id, app_date) in appointment_date:
			try:
				grouped_app[app_date].append(app_id)
			except Exception:
				grouped_app[app_date] = []
				grouped_app[app_date].append(app_id)
				continue

		zabuto_json = []

		for app_date, appointment_ids in grouped_app.iteritems():
			try:
				body = '<table><tr>'
				for appointment_id in appointment_ids:
					try:
						appt_details = f.gen_appt_details(appointment_id)


						if g.g_user.getType() == 'Professor':
							body += '<td>Student name: ' + appt_details[0][1] + ' </td>'
						else:
							body += '<td>Student name: ' + appt_details[0][0] + ' </td>'

						body += '<td>Schedule range: ' + appt_details[0][4] + ' - ' + appt_details[0][5] + '</td>'
						body += '<td><a href="#" id="' +appointment_id+ '">More...</a></td>'

					except Exception:
						continue

				body += '</tr></table>'

				zabuto_datum = {
					'date': app_date.strftime('%Y-%m-%d'),
					'title': 'Appointments',
					'body': body,
					'classname': 'appointments'
				}

				zabuto_json.append(zabuto_datum)
			except Exception:
				continue

		return json.dumps(zabuto_json)
	except Exception, e:
		return json.dumps({'status': 'FAILED', 'msg': str(e)})

def spam_in_get_schedule_table():
	import scripts.functions as f
	import scripts.classes.class_dosql as sql

	g.g_sql = sql.doSql()

	try:
		return json.dumps({'status': 'SUCCESS', 'msg': f.get_schedule_table()})
	except Exception, e:
		return json.dumps({'status': 'FAILED', 'msg': str(e)})
