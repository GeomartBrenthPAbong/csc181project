def index(req):
	import os,sys
	import scripts.third_party_modules.simplejson.simplejson as json
	import global_variables as g

	g.g_main_path = os.path.dirname(__file__)
	sys.path.append(g.g_main_path)

	import functions
	import ajax_functions

	function_name = req.form.getfirst('action')

	try:
		if function_name is None:
			raise Exception
		try:
			if functions.user_logged_in():
				return getattr(ajax_functions, 'spam_in_' + function_name)(req)
			raise AttributeError
		except AttributeError:
				return getattr(ajax_functions, 'spam_out_' + function_name)(req)
	except Exception, e:
		return json.dumps({'status': 'FAILED', 'msg': 'Invalid action'})
