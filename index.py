def index(req, page = 'homepage'):
	import os,sys

	home_path = os.path.dirname(__file__)

	# Just to make sure that our home path is included in the sys.path list
	does_not_exists = False
	for path in sys.path:
		if path == home_path:
			does_not_exists = True
			break
	if does_not_exists is False:
		sys.path.append(home_path)

	import scripts.global_variables
	scripts.global_variables.g_root_path = 'http://localhost/spam'

	scripts.global_variables.g_main_path = home_path

	import scripts.functions

	scripts.global_variables.g_page = page

	scripts.functions.pre_processing()
	scripts.functions.post_processing()

	return scripts.global_variables.g_header.generateHeader() + \
		   scripts.global_variables.g_content.generateContent() + \
		   scripts.global_variables.g_footer.generateFooter()
