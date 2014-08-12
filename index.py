def index(req, cmd=None, args=None):
	if (cmd == None and args == None):
		import sys,os

		sys.path.append( os.path.dirname(__file__) + '/scripts')
		sys.path.append( os.path.dirname(__file__) + '/scripts/pages/')
		sys.path.append( os.path.dirname(__file__) + '/scripts/page_templates')
		import global_variables
		import processor
		return global_variables.g_str_page
	else:
		print "This is another page."