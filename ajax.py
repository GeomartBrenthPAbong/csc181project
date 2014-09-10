def index(req):
	import os,sys,cgi

	sys.path.append( os.path.dirname(__file__) )

	#import functions
	from third_party_modules.simplejson.simplejson.encoder import JSONEncoder

	values = cgi.FieldStorage()

	result = {'msg': values.getvalue('the_value', 'error') }

	return JSONEncoder().encode( result )
	#return json.dumps(response)
	#values = cgi.FieldStorage
	#function_name = values['action']
	#if( functions.is_user_logged_in() ):
	#	try:
	#		return getattr( functions, 'spam_in_' + function_name )
	#	except AttributeError:
	#		return getattr( functions, 'spam_out_' + function_name )
	#else:
	#	try:
	#		return getattr( functions, 'spam_out_' + function_name )
	#	except AttributeError:
	#		response = dict
	#		response['status'] = 'FAILED'
	#		response['error'] = 'Function does not exists'
	#		return json.dumps( response )
