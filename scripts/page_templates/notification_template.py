import scripts.global_variables as g


def generate_page():
	# Styles
	g.g_header.getStyleAdder().add('default_template')

	# Header area
	generated_page = '<div id="header" class="navbar navbar-inverse navbar-fixed-top" role="navigation">' +\
						'<div class="container">' +\
						g.g_locations.printContentsAtLocation('before_nav_bar') +\
						'<div class="navbar-brand-container">' +\
							'<a class="navbar-brand" href="#">'+ g.g_locations.printContentsAtLocation('navbar_brand') +'</a>' +\
						'</div><!-- end navbar-header -->' +\
						'<div class="collapse navbar-collapse navbar-container">' +\
							g.g_locations.printContentsAtLocation('main_nav') +\
						'</div><!-- end navbar -->' +\
						g.g_locations.printContentsAtLocation('after_nav_bar') +\
						'</div><!-- end container -->' +\
					  '</div><!-- end header -->'

	# Content area
	generated_page += '<div id="content">' +\
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

	# Footer area
	generated_page += '<div id="footer">' +\
						'<div class="container">' +\
							g.g_locations.printContentsAtLocation('footer') +\
						'</div><!-- container -->' +\
					 '</div><!-- end footer'

	return generated_page