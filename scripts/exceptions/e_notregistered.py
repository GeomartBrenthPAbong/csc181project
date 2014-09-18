import scripts.exceptions.e_spam as spam


class ENotRegistered(spam.ESpam):
	def __init__(self, message='User not registered'):
		self._m_message = message