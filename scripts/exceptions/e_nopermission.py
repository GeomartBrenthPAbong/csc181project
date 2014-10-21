import scripts.exceptions.e_spam as spam


class ENoPermission(spam.ESpam):
	def __init__(self, p_message='You have no permission to execute this action.'):
		self._m_message = p_message