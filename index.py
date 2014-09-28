def index(req, page = 'home'):
	import os,sys

	home_path = os.path.dirname(__file__)

	# Just to make sure that our home path is included in the sys.path list

	if sys.path.count(home_path) <= 0:
		sys.path.append(home_path)

	import scripts.global_variables
	import scripts.functions
	import scripts.general_additions

	scripts.global_variables.g_root_path = 'http://localhost/spam'
	scripts.global_variables.g_main_path = home_path

	scripts.functions.page_validation( page )

	scripts.functions.pre_processing()
	scripts.general_additions.include_in_pages()
	scripts.functions.process_page()
	scripts.functions.post_processing()

	return scripts.global_variables.g_header.generateHeader() + \
		   scripts.global_variables.g_content.generateContent() + \
		   scripts.global_variables.g_footer.generateFooter()
