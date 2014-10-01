import scripts.global_variables as g


def generate_page():
	# Content area
	generated_page = '<div id="content">' +\
						'<div class="container">' +\
							g.g_locations.printContentsAtLocation('before_title') +\
							'<h2 class="title">' + g.g_content.getTitle() + '</h2>' +\
							g.g_locations.printContentsAtLocation('between_title_content') +\
							'<div class="main-content">' +\
								g.g_content.getContent() +\
							'</div><!-- end main-content -->' +\
							g.g_locations.printContentsAtLocation('after_content') +\
						'</div><!-- container -->' +\
					 '</div><!-- end content'

	return generated_page