def index(req):
	import os,sys
	import scripts.third_party_modules.simplejson.simplejson as json

	sys.path.append(os.path.dirname(__file__))

	import functions
	import ajax_functions

	function_name = req.form.getfirst('action')

	try:
		if function_name is None:
			raise Exception
		if functions.is_user_logged_in():
			try:
				return getattr(ajax_functions, 'spam_in_' + function_name)(req)
			except AttributeError:
				return getattr(ajax_functions, 'spam_out_' + function_name)(req)
		else:
			return getattr(ajax_functions, 'spam_out_' + function_name)(req)
	except Exception, e:
		return json.dumps({'status': 'FAILED', 'msg': 'Invalid action'})
