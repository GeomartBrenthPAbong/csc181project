import class_printable as p


class Form(p.Printable):
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
		return self._m_string

	def generateForm(self, p_include_form_tag = True):
		if p_include_form_tag:
			self._m_string = '<form id="' + self.__m_form_id + '" class="' + self.__m_form_class + '" ' +\
									  'name="' + self.__m_form_name + '">'
		for field in self.__m_form_fields:
			if not 'id' in field:
				field['id'] = ''

			if not 'name' in field:
				field['name'] = ''

			if not 'class' in field:
				field['class'] = ''

			if not 'value' in field:
				field['value'] = ''

			if not 'placeholder' in field:
				field['placeholder'] = ''

			if 'before-field' in field:
				self._m_string += field['before-field']

			if 'label' in field:
						self._m_string += '<label for="' + field['id'] + '">' + field['label'] + '</label>'

			if 'label-field-sep' in field:
						self._m_string += field['label-field-sep']

			if 'type' in field:
				if field['type'] is 'text':

					self._m_string +=  '<input type="text"' +\
												'name="' + field['name']+ '" ' +\
												'id="' + field['id'] + '" ' +\
												'class="' + field['class'] + '" ' +\
												'placeholder="' + field['placeholder'] + '" ' +\
												'value="' + field['value'] + '" />'

				elif field['type'] is 'hidden':
					self._m_string +=  '<input type="hidden"' +\
												'name="' + field['name']+ '" ' +\
												'id="' + field['id'] + '" ' +\
												'class="' + field['class'] + '" ' +\
												'placeholder="' + field['placeholder'] + '" ' +\
												'value="' + field['value'] + '" />'

				elif field['type'] is 'submit':
					self._m_string +=  '<input type="submit"' +\
												'name="' + field['name']+ '" ' +\
												'id="' + field['id'] + '" ' +\
												'class="' + field['class'] + '" ' +\
												'placeholder="' + field['placeholder'] + '" ' +\
												'value="' + field['value'] + '" />'

				elif field['type'] is 'email':
					required = ''
					if 'required' in field and field['required'] is True:
						required = ' required '

					autofocus = ''
					if 'autofocus' in field and field['autofocus'] is True:
						autofocus = ' autofocus '

					self._m_string +=  '<input type="email"' +\
												'name="' + field['name']+ '" ' +\
												'id="' + field['id'] + '" ' +\
												'class="' + field['class'] + '" ' +\
												'placeholder="' + field['placeholder'] + '" ' +\
												'value="' + field['value'] + '" ' + required + autofocus + '/>'

				elif field['type'] is 'password':
					required = ''
					if 'required' in field and field['required'] is True:
						required = ' required '

					autofocus = ''
					if 'autofocus' in field and field['autofocus'] is True:
						autofocus = ' autofocus '

					self._m_string +=  '<input type="password"' +\
												'name="' + field['name']+ '" ' +\
												'id="' + field['id'] + '" ' +\
												'class="' + field['class'] + '" ' +\
												'placeholder="' + field['placeholder'] + '" ' +\
												'value="' + field['value'] + '" ' + required + autofocus + '/>'

				elif field['type'] is 'textarea':
					if not 'rows' in field:
						field['rows'] = ''

					if not 'cols' in field:
						field['cols'] = ''

					self._m_string += '<textarea rows="' + field['rows']+ '" ' +\
												'cols="' + field['cols']+ '" ' +\
												'id="' + field['id'] + '"' +\
												'class="' + field['class'] + '"' +\
												'placeholder="' + field['placeholder'] + '" ' +\
												'name="' + field['name'] + '">' +\
												field['value'] + '</textarea>'

				elif field['type'] is 'radio':

					if 'options' in field and field['options']:

						if not 'option-sep' in field:
							field['option-sep'] = ''

						for option in field['options']:
							if not 'id' in option:
								option['id'] = ''

							if not 'value' in option:
								option['value'] = ''

							if not 'label' in option:
								option['label'] = ''

							misc = ''
							if option['value'] == field['value']:
								misc = ' checked="checked" '

							self._m_string += '<input type="radio" ' +\
														' name="' + field['name'] + '" ' +\
														' class="' + field['class']+ '" ' +\
														' value="' + option['value']+ '" ' +\
														' id="' + option['id'] + '" ' + misc + '/>' +\
														'<label for="' + option['id'] + '">' +\
														option['label'] +\
														'</label>'

							self._m_string += field['option-sep']

				elif field['type'] is 'checkbox':

					if 'options' in field and field['options']:

						if not 'option-sep' in field:
							field['option-sep'] = ''

						for option in field['options']:
							if not 'id' in option:
								option['id'] = ''

							if not 'value' in option:
								option['value'] = ''

							if not 'label' in option:
								option['label'] = ''

							misc = ''
							if option['value'] == field['value']:
								misc = ' checked="checked" '

							self._m_string += '<input type="checkbox" ' +\
														' name="' + field['name'] + '" ' +\
														' class="' + field['class']+ '" ' +\
														' value="' + option['value']+ '" ' +\
														' id="' + option['id'] + '" ' + misc + '/>' +\
														'<label for="' + option['id'] + '">' +\
														option['label'] +\
														'</label>'

							self._m_string += field['option-sep']

				elif field['type'] is 'select':

					if 'options' in field and field['options']:
						self._m_string += '<select name="' + field['name'] + '" ' +\
														'id="' + field['id']+ '" ' +\
														'class="' + field['class'] + '">'

						for option in field['options']:

							if not 'class' in option:
								option['class'] = ''

							if not 'value' in option:
								option['value'] = ''

							if not 'label' in option:
								option['label'] = ''

							misc = ''
							if option['value'] is field['value']:
								misc = 'selected'

							self._m_string += '<option value="' +option['value']+ '" ' + misc + '>' +\
														option['label'] +\
														'</option>'

						self._m_string += '</select>'

			if 'after-field' in field:
				self._m_string += field['after-field']

		if p_include_form_tag:
			self._m_string += '</form>'

	def toString(self):
		self.generateForm();
		return self._m_string
