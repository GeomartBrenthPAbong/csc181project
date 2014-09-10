import scripts.global_variables
import scripts.classes.class_header
import scripts.classes.class_content
import scripts.classes.class_footer
import scripts.classes.class_locations
import scripts.classes.class_printable
import scripts.classes.classes_menu

def include_in_pages():
	from scripts.third_party_modules.ordereddict.ordereddict import OrderedDict

	scripts.global_variables.g_header.getStyleAdder().add('styles')

	scripts.global_variables.g_header.getScriptAdder().add('jquery-2.1.1.min')
	scripts.global_variables.g_header.getScriptAdder().add('general')

	scripts.global_variables.g_locations.addToLocation('just_after_body_tag',
														scripts.classes.class_printable.Printable('<div><p>Added first. Printed to every page</p></div>'))
	scripts.global_variables.g_locations.addToLocation('just_after_body_tag',
														scripts.classes.class_printable.Printable('<div><p>Added second. Printed to every page</p></div>'), 5)
	scripts.global_variables.g_locations.addToLocation('just_after_body_tag',
														scripts.classes.class_printable.Printable('<div><p>Added third. Printed to every page</p></div>'), 12)
	scripts.global_variables.g_locations.addToLocation('just_after_body_tag',
														scripts.classes.class_printable.Printable('<div><p>Added fourth. Printed to every page</p></div>'), 1)
	scripts.global_variables.g_locations.addToLocation('content_custom_location',
														scripts.classes.class_printable.Printable('<div><p>For custom location. Printed to every page</p></div>'), 1)

	menu_items = OrderedDict([('link_1', { 'label': 'Test link one',
										   'link': '#'}),
								('link_2', { 'label': 'Test link two',
											 'link': '#'} ),
								('link_3', { 'label': 'Test link three',
											   'link': 'http://www.google.com'})]);

	menu = { 'before_ul': '<p>Before Menu</p>',
			 'after_ul': '<p>After Menu</p>',
			 'before_li': '<span class="before-li"></span>',
			 'after_li': '<span class="after-li"></span>',
			 'before_a': '<span class="before-a"></span>',
			 'after_a': '<span class="after-a"></span>',
			 'inside_a': '<span class="inside-a"></span>',
			 'ul_id': 'main-menu',
			 'ul_class': 'site-menu',
			 'li_class': 'main-menu-item',
			 'a_class': 'main-menu-item-link',
			 'menu_items': menu_items
			}

	scripts.global_variables.g_locations.addToLocation('main_menu', scripts.classes.classes_menu.Menu(menu))