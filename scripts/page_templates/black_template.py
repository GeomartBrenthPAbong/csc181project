import scripts.global_variables as g


def generate_page():
	# Styles
	g.g_header.getStyleAdder().add('black_template')

	#Scripts
	g.g_header.getScriptAdder().add('black_template')

	# Header area
	blocker = """
			<div id="blocker">
			</div>
			"""
	modal_container = """
					<div id="modal-container">
						<div id="modal-holder">
							<div id="modal">
								<button id="modal-close" type="button" class="close"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
								<table class="table table-hover">
								<thead>
									<tr>
										<th id="modal-header">Header</th>
									</tr>
						  		</thead>
								</table>
								<div id="modal-body"></div>
								<div id="modal-footer"></div>
							</div>
						</div>
					</div>
					"""

	# Header area
	generated_page = '<div class="page-wrap">' + blocker + modal_container + '<div id="header">' +\
						'<div class="container">' +\
						'<div class="navbar-container">' +\
							g.g_locations.printContentsAtLocation('main_nav') +\
						'</div><!-- end navbar-header -->' +\
						'<div class="logo">' +\
							'<a href="#">'+ g.g_locations.printContentsAtLocation('navbar_brand') +'</a>' +\
						'</div><!-- end navbar -->' +\
						'<span class="clearfix"></span>' +\
						'</div><!-- end container -->' +\
					  '</div><!-- end header -->'

	# Content area
	generated_page += '<div id="content">' +\
						'<div class="container">' +\
								'<div class="left-content left"><div class="wrapper"><span class="absolute arrow arrow-left"></span><div>' +\
									g.g_content.getContent() +\
									g.g_locations.printContentsAtLocation('left_content') +\
								'</div></div></div>' +\
								'<div class="right-content right"><div class="wrapper"><span class="absolute arrow arrow-right"></span>' +\
									g.g_locations.printContentsAtLocation('before_title') +\
									'<h2 class="title">' + g.g_content.getTitle() + '</h2>' +\
									g.g_locations.printContentsAtLocation('between_title_content') +\
									'<div>' +\
									g.g_locations.printContentsAtLocation('right_content') +\
								'</div></div></div>' +\
								'<div class="absolute right-bg"><div class="rel"><span class="absolute"></span></div></div>' +\
								'<div class="clearfix"></div>' +\
							g.g_locations.printContentsAtLocation('after_content') +\
						'</div><!-- container -->' +\
					 '</div><!-- end content-->'

	# Footer area
	generated_page += '<div id="footer">' +\
						'<div class="container">' +\
							g.g_locations.printContentsAtLocation('footer') +\
						'</div><!-- container -->' +\
					 '</div><!-- end footer -->' +\
					'</div><!-- end page-wrap -->'

	return generated_page