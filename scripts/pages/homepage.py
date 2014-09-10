import scripts.global_variables

def get_title():
	return 'Homepage'

def get_content():
	return 'Hello World <a href="#" class="test">Click Here</a>'

def get_page_template():
	return 'default'

def page_additions():
	from scripts.third_party_modules.ordereddict.ordereddict import OrderedDict
	from scripts.classes.classes_menu import Menu

	main_menu_list = scripts.global_variables.g_locations.getContentsAtLocation('main_menu')
	if not main_menu_list is None:
		if len(main_menu_list) == 1: # insert checking if of Type Menu
			main_menu = main_menu_list[0]

			sub_sub_menu = Menu({'menu_items': OrderedDict([('ssm1', { 'label': 'SUBSUB MENU 1',
																	  'link': '#'}),
															('ssm2', { 'label': 'SUBSUB MENU 2',
																	   'link': '#'})])})

			link_one_sub_menu = Menu({'menu_items': OrderedDict([('sub_1', { 'label': 'Submenu 1',
										   'link': '#',
										   'sub_menu': sub_sub_menu}),
									   ('sub_2', { 'label': 'Submenu 2',
											 'link': '#'} ),
									   ('sub_3', { 'label': 'Submenu 3',
											   'link': 'http://www.google.com'})])})

			menu_items = OrderedDict([('link_5', { 'label': 'Test link five',
										   'link': '#'}),
									   ('link_6', { 'label': 'Test link six',
											 'link': '#'} ),
									   ('link_7', { 'label': 'Test link seven',
											   'link': 'http://www.google.com'})])

			main_menu.addToMenu(menu_items)
			main_menu.addAsSubmenu('link_1', link_one_sub_menu)

			main_menu.addMenuItem('link_4', 'Added in homepage', '#')
			scripts.global_variables.g_locations.clearLocation('main_menu')
			scripts.global_variables.g_locations.addToLocation('main_menu', main_menu)

	scripts.global_variables.g_footer.getScriptAdder().add('temp')
	scripts.global_variables.g_locations.addToLocation('just_after_body_tag',
														scripts.classes.class_printable.Printable('<div><p>Exclusive for homepage only</p></div>'))


