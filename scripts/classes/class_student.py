import class_user as user

class Student(user.User):
	def __init__(self):
		self.__m_course = None
		
	def setCourse(self, p_stud_course):
		self.__m_course = p_stud_course
		
	def getCourse(self):
		return self.__m_course