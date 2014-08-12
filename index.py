import sys
import os

def index(req, cmd=None, args=None):
	if (cmd == None and args == None):
		import global_variables
		import postprocessor
		return global_variables.g_str_page
	else:
		print "This is another page."
