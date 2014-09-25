import scripts.global_variables as g
import scripts.classes.class_printable as p

def get_title():
	return 'Appointments'

def get_content():
	html =	"""
	<div id="content">
   <div id="tab-container">
      <ul>
         <li><a href="http://bobcravens.com/demos/vertical_tabs/index.html">Introduction</a></li>
         <li><a href="http://bobcravens.com/demos/vertical_tabs/html.html">Html</a></li>
         <li><a href="http://bobcravens.com/demos/vertical_tabs/style.html">CSS</a></li>
         <li><a href="http://bobcravens.com/demos/vertical_tabs/script.html">JavaScript</a></li>
      </ul>
   </div>
   <div id="main-container">
      <h1>Put your content here...</h1>
   </div>
</div>
			"""

	return html


def get_page_template():
	return 'black_template'

def page_additions():
	# Styles and Scripts additions here

	# Location additions here

	#### head_title Location addition
	g.g_locations.addToLocation('head_title', p.Printable(g.g_content.getTitle()))

	# Default changes here
	content_list = g.g_locations.getContentsAtLocation('main_nav')
	if len(content_list) is 1:
		main_nav = content_list[0]
		main_nav.setAsActive('home')


