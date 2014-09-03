import scripts.global_variables

def processPage():
	scripts.global_variables.g_content.setTitle('------ Sample Page --------')
	scripts.global_variables.g_content.setContent('This is the sample page!')
	scripts.global_variables.g_content.setPageTemplate('default')

scripts.global_variables.g_process_page = processPage