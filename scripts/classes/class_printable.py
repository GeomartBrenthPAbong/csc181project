class Printable(object):
	def __init__(self, p_string = ''):
		self._m_string = p_string

	def setString(self, p_string):
		self._m_string = p_string

	def toString(self):
		return self._m_string
