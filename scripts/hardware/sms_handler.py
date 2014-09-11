"""
this script is used for creating a thread to
send a message. the thread is terminated
after the message is sent.
one thread for one message
"""

import globvars

class SmsSenderThread(threading.Thread):
	def __init__(self, p_number, p_message):
		threading.Thread.__init__(self)
		
	def run(self):
		try:
			globvars.ser.write(p_number + "#" + p_message)
			return 1
		except:
			return 1