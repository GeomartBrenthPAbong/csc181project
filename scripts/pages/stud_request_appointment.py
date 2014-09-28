import scripts.global_variables as g
import scripts.classes.class_printable as p

def get_title():
	return 'Request Appointment'

def get_content():
	html =	"""
	    <!doctype html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <title>sim</title>
        <link rel="stylesheet" href="../css/search_style.css">
        </head>
        <body>
        <div id="gradient"></div>
        <form class="searchbox" action="">
        <input type="search" placeholder="Search Professor" />
        <button type="submit" value="search">&nbsp;</button>
        </form>
        </body>
        </html>
			"""

	return html

def get_page_template():
	return 'black_template'

def page_additions():
	pass
