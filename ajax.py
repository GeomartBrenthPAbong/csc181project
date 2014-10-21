def index(req):
	import os,sys
	import scripts.third_party_modules.simplejson.simplejson as json

	main_path = os.path.dirname(__file__)
	sys.path.append(main_path)

	import scripts.global_variables as g
	import scripts.functions as functions
	import scripts.ajax_functions as ajax_functions

	g.g_root_path = 'http://localhost/spam'
	g.g_main_path = main_path

	function_name = req.form.getfirst('action')

	g.g_req = req
	g.f_ajax_req = True
	g.g_user = functions.create_user()

	try:
		if function_name is None:
			raise Exception
		try:
			if functions.user_logged_in():
				return getattr(ajax_functions, 'spam_in_' + function_name)()
			raise AttributeError
		except AttributeError:
				return getattr(ajax_functions, 'spam_out_' + function_name)()
	except Exception, e:
		return json.dumps({'status': 'FAILED',
						   'type': 'function_existence',
						   'msg': 'Either your have no permission to execute this action or there is no handler for this action.'})
