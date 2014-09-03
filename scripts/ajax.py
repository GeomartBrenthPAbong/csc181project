import functions
import cgi
import json

def exceute():
	values = cgi.FieldStorage
	function_name = values['action']
	if( functions.is_user_logged_in() ):
		try:
			return getattr( functions, 'spam_in_' + function_name )
		except AttributeError:
			return getattr( functions, 'spam_out_' + function_name )
	else:
		try:
			return getattr( functions, 'spam_out_' + function_name )
		except AttributeError:
			response = dict
			response['status'] = 'FAILED'
			response['error'] = 'Function does not exists'
			return json.dumps( response )