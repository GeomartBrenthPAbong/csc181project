import scripts.global_variables

def processTemplate():
	scripts.global_variables.g_str_body = '<div><p>home template ' + scripts.global_variables.g_str_content + '</p></div>'

scripts.global_variables.g_process_template = processTemplate
