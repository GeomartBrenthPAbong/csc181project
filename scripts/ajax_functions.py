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
	import third_party_modules.simplejson.simplejson as json
	import functions as f

	return json.dumps({'status': 'SUCCESS', 'msg': f.gen_prof_list(g.g_req) })