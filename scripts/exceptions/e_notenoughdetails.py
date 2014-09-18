import scripts.exceptions.e_spam as spam


class ENotEnoughDetails(spam.ESpam):
	def __init__(self, message='Not enough details'):
		self._m_message = message