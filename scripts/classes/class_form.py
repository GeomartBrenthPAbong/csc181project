class Form(object):
	def __init__(self,
				 p_id = '',
				 p_class = '',
				 p_name = '',
				 p_method = 'POST'):
		self.__m_form_id = p_id
		self.__m_form_class = p_class
		self.__m_form_name = p_name
		self.__m_form_method = p_method
		self.__m_form_fields = []
		self.__m_generated_form = ''

	def setFormID(self, p_id):
		self.__m_form_id = p_id

	def setFormClass(self, p_class):
		self.__m_form_class = p_class

	def setFormName(self, p_name):
		self.__m_form_name = p_name

	def setFormMethod(self, p_method):
		self.__m_form_method = p_method

	def setFields(self, p_fields):
		self.__m_form_fields = p_fields

	def getFormID(self):
		return self.__m_form_id

	def getFormClass(self):
		return self.__m_form_class

	def getFormName(self):
		return self.__m_form_name

	def getFormMethod(self):
		return self.__m_form_method

	def getGeneratedForm(self):
		return self.__m_generated_form

	def generateForm(self, p_include_form_tag = True):
		if p_include_form_tag:
			self.__m_generated_form = '<form id="' + self.__m_form_id + '" class="' + self.__m_form_class + '" ' +\
									  'name="' + self.__m_form_name + '">'
		for field in self.__m_form_fields:
			if not 'id' in self.__m_form_fields:
				self.__m_form_fields['id'] = ''
			if not 'name' in self.__m_form_fields:
				self.__m_form_fields['name'] = ''
			if not 'class' in self.__m_form_fields:
				self.__m_form_fields['class'] = ''
			if not 'value' in self.__m_form_fields:
				self.__m_form_fields['value'] = ''

			if 'before-field' in self.__m_form_fields:
				self.__m_generated_form += self.__m_form_fields['before-field']

			if 'type' in self.__m_form_fields:
				if self.__m_form_fields['type'] == 'text':
					if 'label' in self.__m_form_fields:
						self.__m_generated_form += '<label for="' + self.__m_form_fields['id'] + '">' + self.__m_form_fields['label'] + '</label>'
					self.__m_generated_form +=  '<input type="text" +\ ' \
											    'name="' + self.__m_form_fields['name']+ '" ' +\
											    'id="' + self.__m_form_fields['id'] + '" ' +\
											    'class="' + self.__m_form_fields['class'] + '" ' +\
											    'value="' + self.__m_form_fields['value'] + '" />'
				if self.__m_form_fields['type'] == 'hidden':
					if 'label' in self.__m_form_fields:
						self.__m_generated_form += '<label for="' + self.__m_form_fields['id'] + '">' + self.__m_form_fields['label'] + '</label>'
					self.__m_generated_form +=  '<input type="hidden" +\ ' \
											    'name="' + self.__m_form_fields['name']+ '" ' +\
											    'id="' + self.__m_form_fields['id'] + '" ' +\
											    'class="' + self.__m_form_fields['class'] + '" ' +\
											    'value="' + self.__m_form_fields['value'] + '" />'
				if self.__m_form_fields['type'] == 'submit':
					if 'label' in self.__m_form_fields:
						self.__m_generated_form += '<label for="' + self.__m_form_fields['id'] + '">' + self.__m_form_fields['label'] + '</label>'
					self.__m_generated_form +=  '<input type="submit" +\ ' \
											    'name="' + self.__m_form_fields['name']+ '" ' +\
											    'id="' + self.__m_form_fields['id'] + '" ' +\
											    'class="' + self.__m_form_fields['class'] + '" ' +\
											    'value="' + self.__m_form_fields['value'] + '" />'
		if p_include_form_tag:
			self.__m_generated_form += '</form>'

