import global_variables as g
import third_party_modules.simplejson.simplejson as json

def spam_in_test_ajax(req):

	import third_party_modules.simplejson.simplejson as json

	###=============== For future use

	#import Cookie
	#import functions
	#import classes.class_user_factory as user_factory
	#import exceptions.e_notregistered as e_notregistered
	#import global_variables as g
	#
	#try:
	#	g.g_user = user_factory.UserFactory().createUser(req.form.getfirst('username'), req.form.getfirst('password'))
	#except e_notregistered.ENotRegistered, e:
	#	return json.dumps({'status': 'SUCCESS', 'msg': e.getMessage()})

	#functions.setup_cookies(req.form.getfirst('username'))
	#cookie = Cookie.SimpleCookie()

	#functions.setup_cookies()

	##====================

	return json.dumps({'status': 'SUCCESS',
						'msg': 'Username: ' + req.form.getfirst('username') +\
								' Password: ' + req.form.getfirst('password')})

def spam_out_add_schedule(req):
	import scripts.classes.class_user_factory as uf
	import scripts.classes.class_schedule as s
	import scripts.exceptions.e_spam as espam
	import scripts.classes.class_dosql as sql

	from_time = req.form.getfirst('from_time')
	to_time = req.form.getfirst('to_time')
	day = req.form.getfirst('day')
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

def spam_out_get_page_content(req):
	import functions as f

	g.g_page_name = req.form.getfirst('page_name')
	page_locations = json.loads(req.form.getfirst('page_location'))

	f.page_validation(g.g_page_name)
	if g.g_page_name == 'notification':
		return json.dumps({'status': 'FAILED', 'data': {
			'title': g.g_notification_title,
			'right_content': g.g_notification_msg
		}})

	f.pre_processing()
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


def spam_in_gen_prof_list(req):
	import third_party_modules.simplejson.simplejson as json
	import functions as f

	return json.dumps({'status': 'SUCCESS', 'msg': f.gen_prof_list(req)})
