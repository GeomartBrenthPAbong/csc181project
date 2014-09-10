import scripts.global_variables

def get_title():
	return 'Sample Page'

def get_content():
	return 'This is the sample page'

def get_page_template():
	return 'default'

def page_additions():
	scripts.global_variables.g_locations.addToLocation('just_after_body_tag',
														scripts.classes.class_printable.Printable('<div><p>Exclusive for samplepage</p></div>'))


