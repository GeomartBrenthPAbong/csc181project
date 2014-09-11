import class_printable


class Menu(class_printable.Printable):
	def __init__(self, p_menu = None):
		self.__m_menu = p_menu
		super(Menu, self).__init__()

	def setMenu(self, p_menu):
		self.__m_menu = p_menu

	def setMenuID(self, p_menu_id):
		if self.__m_menu is None:
			return
		self.__m_menu['ul_id'] = p_menu_id

	def getGeneratedMenu(self):
		return self._m_string

	def getMenuID(self):
		if self.__m_menu is None or not 'ul_id' in self.__m_menu:
			return None
		return self.__m_menu['ul_id']

	def getMenuItems(self):
		if self.__m_menu is None or not 'menu_items' in self.__m_menu:
			return None
		return self.__m_menu['menu_items']

	# OrderedDict p_menu_items is of the format: { 'id here': {
	# 													'label': label here
	# 													'link': link here
	# 													'sub_menu': submrenu here}}
	def addToMenu(self, p_menu_items):
		if self.__m_menu is None or not 'menu_items' in self.__m_menu:
			self.__m_menu = {}

		self.__m_menu['menu_items'].update(p_menu_items)

	def addMenuItem(self, p_menu_item_id, p_menu_item_label, p_menu_item_link, p_menu_item_sub = None):
		if self.__m_menu is None or not 'menu_items' in self.__m_menu:
			self.__m_menu = {}

		menu_item = {}
		menu_item[p_menu_item_id] = {'label': p_menu_item_label,
									 'link': p_menu_item_link}
		if not p_menu_item_sub is None:
			menu_item['sub_menu'] = p_menu_item_sub

		self.__m_menu['menu_items'].update(menu_item)

	def addAsSubmenu(self, p_parent_menu_id, p_menu):
		if self.__m_menu is None \
		   or not 'menu_items' in self.__m_menu \
		   or not p_parent_menu_id in self.__m_menu['menu_items']:
				return

		self.__m_menu['menu_items'][p_parent_menu_id]['sub_menu'] = p_menu

	def removeSubmenu(self, p_menu_id):
		if p_menu_id in self.__m_menu['menu_items']:
			if 'sub_menu' in self.__m_menu['menu_items'][p_menu_id]:
				del self.__m_menu['menu_items'][p_menu_id]['sub_menu']
				return
		self.__removeSubmenuH(p_menu_id, self.__m_menu['menu_items'])

	def __removeSubmenuH(self, p_menu_id, p_menu):
		if p_menu_id in p_menu:
				if 'sub_menu' in p_menu[p_menu_id]:
					del p_menu[p_menu_id]['sub_menu']
				return True

		for menu_item_key in p_menu:
			if 'sub_menu' in p_menu[menu_item_key]:
				if self.__removeSubmenuH(p_menu_id, p_menu[menu_item_key]['sub_menu'].getMenuItems()):
					return True
		return False

	def removeMenuItem(self, p_menu_id):
		if p_menu_id in self.__m_menu['menu_items']:
			del self.__m_menu['menu_items'][p_menu_id]
			return
		self.__removeMenuItemH(p_menu_id, self.__m_menu['menu_items'])

	def __removeMenuItemH(self, p_menu_id, p_menu):
		if p_menu_id in p_menu:
				del p_menu[p_menu_id]
				return True

		for menu_item_key in p_menu:
			if 'sub_menu' in p_menu[menu_item_key]:
				if self.__removeMenuItemH(p_menu_id, p_menu[menu_item_key]['sub_menu'].getMenuItems()):
					return True
		return False

	def generateMenu(self):
		if self.__m_menu is None \
		   or not 'menu_items' in self.__m_menu:
			return

		if 'before_ul' in self.__m_menu:
			self._m_string = self.__m_menu['before_ul']

		self._m_string += '<ul'
		if 'ul_id' in self.__m_menu:
			self._m_string += ' id="'+self.__m_menu['ul_id']+'" '
		if 'ul_class' in self.__m_menu:
			self._m_string += ' class="menu '+self.__m_menu['ul_class']+'" '
		self._m_string += '>'

		before_li = ''
		if 'before_li' in self.__m_menu:
			before_li = self.__m_menu['before_li']

		after_li = ''
		if 'after_li' in self.__m_menu:
			after_li = self.__m_menu['after_li']

		li_class = ''
		if 'li_class' in self.__m_menu:
			li_class = self.__m_menu['li_class']

		before_a = ''
		if 'before_a' in self.__m_menu:
			before_a = self.__m_menu['before_a']

		after_a = ''
		if 'after_a' in self.__m_menu:
			after_a = self.__m_menu['after_a']

		a_class = ''
		if 'a_class' in self.__m_menu:
			a_class = self.__m_menu['a_class']

		inside_a = ''
		if 'inside_a' in self.__m_menu:
			inside_a = self.__m_menu['inside_a']

		for menu_item_dict in self.__m_menu['menu_items']:
			menu_item = self.__m_menu['menu_items'][menu_item_dict]
			if not 'label' in menu_item:
				continue

			link = '#'
			if 'link' in menu_item:
				link = menu_item['link']

			self._m_string += before_li +\
								'<li class="menu-item '+li_class+'">' +\
									before_a+'<a href="'+link+'" class="menu-item-link '+a_class+'">' +\
											menu_item['label'] + inside_a +\
									'</a>'+after_a


			if 'sub_menu' in menu_item:
				self._m_string += menu_item['sub_menu'].toString()

			self._m_string += '</li>'+after_li

		self._m_string += '</ul>'

		if 'after_ul' in self.__m_menu:
			self._m_string += self.__m_menu['after_ul']

	def toString(self):
		self.generateMenu()
		return self._m_string


