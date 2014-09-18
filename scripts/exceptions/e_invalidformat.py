import scripts.exceptions.e_spam as spam


class EInvalidFormat(spam.ESpam):
	def __init__(self, p_message='Invalid format.'):
		self._m_message = p_message