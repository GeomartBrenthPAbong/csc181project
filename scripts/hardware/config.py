"""
This python program is used to
configure the com port settings.
The configuration settings are
saved in config.txt file.
""" 
import globvars, sms_methods

print "Configuration for SPAM SMS Feature."
globvars.com_port = input("COM PORT: ")
sms_methods.initialize_serial_com(globvars.com_port)