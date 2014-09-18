class ESpam(Exception):
	def __init__(self, message='Standard SPAM problem.'):
		self._m_message = message

	def getMessage(self):
		return self._m_message