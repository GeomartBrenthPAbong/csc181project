import scripts.exceptions.e_spam as spam


class EAlreadyExists(spam.ESpam):
	def __init__(self, p_message='Already exists'):
		self._m_message = p_message