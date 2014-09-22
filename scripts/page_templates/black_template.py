import scripts.global_variables as g


def generate_page():
	# Styles
	g.g_header.getStyleAdder().add('black_template')

	#Scripts
	g.g_header.getScriptAdder().add('black_template')

	# Header area
	generated_page = '<div class="page-wrap"><div id="header">' +\
						'<div class="container">' +\
						'<div class="navbar-brand-container left">' +\
							'<a class="navbar-brand" href="#">'+ g.g_locations.printContentsAtLocation('navbar_brand') +'</a>' +\
						'</div><!-- end navbar-header -->' +\
						'<div class="navbar-container left"><span class="decoration"></span>' +\
							g.g_locations.printContentsAtLocation('main_nav') +\
						'</div><!-- end navbar -->' +\
						'<span class="clearfix"></span>' +\
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
					 '</div><!-- end footer -->' +\
					'</div><!-- end page-wrap -->'

	return generated_page