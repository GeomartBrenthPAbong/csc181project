import scripts.global_variables as g
import scripts.classes.class_header
import scripts.classes.class_content
import scripts.classes.class_footer
import scripts.classes.class_locations
import scripts.classes.class_printable
import scripts.classes.classes_menu

def include_in_pages():
	# Bootstrap
	g.g_header.getStyleAdder().add('bootstrap/css/bootstrap.min')
	g.g_header.getStyleAdder().add('bootstrap/css/bootstrap-theme.min')

	# Styles for all pages
	g.g_header.getStyleAdder().add('styles')


	# Scripts for all pages


	# Location additions for all pages