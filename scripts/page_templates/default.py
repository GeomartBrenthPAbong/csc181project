import scripts.global_variables

generated_page = '<div id="content" class="content-wrapper wrapper">'
generated_page += '<h2 class="title">' + scripts.global_variables.g_content.getTitle() + '</h2>'
generated_page += '<div id="main-content">' + scripts.global_variables.g_content.getContent() + '</div>'
generated_page += '</div>'

scripts.global_variables.g_content.setGeneratedContent(generated_page)