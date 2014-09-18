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
