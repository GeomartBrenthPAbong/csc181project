import class_user as user


class Student(user.User):

	def __init__(self):
		self.__m_course = None
		self._m_type = 'student'

	def setCourse(self, p_course):
		self.__m_course = p_course

	def getCourse(self):
		return self.__m_course