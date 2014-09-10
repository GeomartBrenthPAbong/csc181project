import scripts.global_variables

def generate_page():
	generated_page = '<div id="content" class="content-wrapper wrapper">'
	generated_page += '<div>'+scripts.global_variables.g_locations.printContentsAtLocation('main_menu')+'</div>'
	generated_page += '<h2 class="title">' + scripts.global_variables.g_content.getTitle() + '</h2>'
	generated_page += '<div id="main-content">' + scripts.global_variables.g_content.getContent() + '</div>'
	generated_page += scripts.global_variables.g_locations.printContentsAtLocation('content_custom_location')
	generated_page += '</div>'
	return generated_page


