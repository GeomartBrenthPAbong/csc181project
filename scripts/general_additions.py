import scripts.global_variables as g
import scripts.classes.class_menu as m
import scripts.third_party_modules.ordereddict.ordereddict as od
import scripts.classes.class_printable as p

def include_in_pages():
	# Bootstrap
	g.g_header.getStyleAdder().add('bootstrap/css/bootstrap.min')
	g.g_header.getStyleAdder().add('bootstrap/css/bootstrap-theme.min')

	# Styles for all pages

	# Scripts for all pages
	g.g_header.getScriptAdder().add('jquery-2.1.1.min')

	# Location additions for all pages

	#### navbar_brand Location addition for default template
	g.g_locations.addToLocation('navbar_brand', p.Printable('S.<br>P.<br>A.<br>M.'))

	#### main_nav location addition for default template
	menu_items = od.OrderedDict([
									('home', {
												'label': 'Home',
												'link': g.g_root_path + '/index.py?page=home'}),
									('calendar', {
												'label': 'Calendar',
												'link': '#'}),
									('appointments', {
												'label': 'Appointments',
												'link': '#'}),
									('settings', {
												'label': 'Settings',
												'link': '#'}),
									('sign_out', {
												'label': 'Sign out',
												'link': '#'})
								])

	menu = { 'ul_class': 'main-nav nav navbar-nav',
			 'before_a': '<div>' +\
						 '<span class="adder blue-adder"></span>' +\
						 '<div class="img-coater">' +\
						 	'<span class="img"></span>'
						 '</div>' +\
						 '<span class="nav-block">%label%</span>',
			 'after_a': '</div>',
			 'li_class': 'main-menu-item',
			 'a_class': 'main-menu-item-link',
			 'menu_items': menu_items
			}

	g.g_locations.addToLocation('main_nav', m.Menu(menu))
