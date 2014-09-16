import scripts.global_variables as g


def generate_page():
	generated_page = '<div id="main-content" class="clean_template">'
	generated_page += '<div class="top title-wrapper"><h1 class="title">' + g.g_locations.printContentsAtLocation('title') + '</h1>'
	generated_page += '<h2 class="sub-title">' + g.g_locations.printContentsAtLocation('sub_title') + ' </h2></div>'
	generated_page += '<div class="bottom main-content-wrapper">'
	generated_page += g.g_locations.printContentsAtLocation('main_content')
	generated_page += '</div><!-- end main-content-wrapper --></div> <!-- end main-content -->'
	return generated_page