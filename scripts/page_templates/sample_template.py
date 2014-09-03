import scripts.global_variables

def processTemplate():
	scripts.global_variables.g_str_body = '<div id="sample-template">sample template ' + scripts.global_variables.g_str_content + '</div>'

scripts.global_variables.g_process_template = processTemplate