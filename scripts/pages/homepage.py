import scripts.global_variables

def processPage():
	scripts.global_variables.g_content.setTitle('Homepage')
	scripts.global_variables.g_content.setContent('Hello World!')
	scripts.global_variables.g_content.setPageTemplate('default')

scripts.global_variables.g_process_page = processPage

