import sys
sys.path.insert(0, 'scripts')
from preprocessor import *

def index(req, cmd=None, args=None):
	if (cmd == None and args == None):
		print test
	else:
		print "This is another page."

