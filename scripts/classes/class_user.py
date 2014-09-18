import scripts.global_variables as g


class User(object):
	def __init__(self):
		self._m_id = None
		self._m_first_name = None
		self._m_last_name = None
		self._m_email_address = None
		self._m_phone_number = None

	##==============================
	## Getters and Setters

	def setUserID(self, p_id ):
		self._m_id = p_id

	def setFirstName(self, p_first_name):
		self._m_first_name = p_first_name

	def setLastName(self, p_last_name):
		self._m_last_name = p_last_name

	def setEmailAddress(self, p_email_address):
		self._m_email_address = p_email_address

	def setPhoneNumber(self, p_phone_number):
		self._m_phone_number = p_phone_number

	def getUserID(self):
		return self._m_id

	def getFirstName(self):
		return self._m_first_name

	def getLastName(self):
		return self._m_last_name

	def getEmailAddress(self):
		return self._m_email_address

	def getPhoneNumber(self):
		return self._m_phone_number

	def getAppointments(self):
		return g.g_sql.execqry('getApptPerUserId(' + self._m_id + ')')

	def getPendingAppointments(self):
		return g.g_sql.execqry('getPendingApptPerUserId(' + self._m_id + ')')




