import scripts.global_variables as g

def get_title():
	if not g.g_notification_title:
		g.g_notification_title = 'Error title'
	return g.g_notification_title

def get_content():
	if not g.g_notification_msg:
		g.g_notification_msg = 'Error message'
	return g.g_notification_msg

def get_page_template():
	return 'notification_template'

def page_additions():
	pass
