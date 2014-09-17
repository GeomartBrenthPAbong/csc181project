"""
This script contains method called by web to send message,
and method called by a python program to initialize serial
communication interface.
"""

import serial
import sms_handler, globvars

def send_message(p_number, p_message):
	try:
		sms_thread = sms_handler.SmsSenderThread(p_number, p_message)
		sms_thread.start()
	except:
		return "Oops! Something's wrong with SMS feature."
		
# Usage: send_message("09123456789", "Test message.")
# Maintain limits for message length
		
def initialize_serial_com(p_com_port):
	try:
		globvars.ser = serial.Serial(port = p_com_port)
	except:
		print "Initialization failed."
		
		
