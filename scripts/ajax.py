def index(req):
	import os,sys
	import scripts.third_party_modules.simplejson.simplejson as json

	sys.path.append(os.path.dirname(__file__))

	import scripts.functions as functions
	import scripts.ajax_functions as ajax_functions

	function_name = req.form.getfirst('action')

	try:
		if function_name is None:
			raise Exception
		if functions.is_user_logged_in():
			try:
				function = getattr(ajax_functions, 'spam_in_' + function_name)(req)
			except AttributeError:
				function = getattr(ajax_functions, 'spam_out_' + function_name)(req)
		else:
			try:
				function = getattr(ajax_functions, 'spam_out_' + function_name)(req)
			except AttributeError:
				raise Exception

		if not function or not callable(function):
				raise Exception
		return function()
	except:
		return json.dumps({'status':'FAILED', 'msg': 'Invalid action'})
