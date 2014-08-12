import sys
import os

def index(req, cmd=None, args=None):
	if (cmd == None and args == None):
		sys.path.append(os.path.dirname(__file__) + '/scripts')
		#var = os.path.dirname(__file__) + 'scripts'
		from preprocessor import *
		return "hello"
	else:
		print "This is another page."

