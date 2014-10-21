import class_user as user


class Student(user.User):

	def __init__(self):
		self.__m_course = None
		self._m_type = 'student'

	def setCourse(self, p_course):
		self.__m_course = p_course

	def getCourse(self):
		return self.__m_course

	def sendAppointmentRequest(self, p_prof_id, p_prof_sched_id, p_date, p_msg):
		import scripts.functions as f
		import scripts.global_variables as g
		import scripts.classes.class_user_factory as uf

		prof = uf.UserFactory().createUserFromID(p_prof_id)

		#Check if prof is available
		prof_availability = g.g_sql.execqry("SELECT * FROM isProfAvailable('"+ str(p_prof_id) +"', " + str(p_prof_sched_id) + ", '" + p_date + "')", False)
		if not f.is_none_list(prof_availability):
			raise Exception('Professor ' + prof.getFirstName() + ' ' + prof.getLastName() + ' is not available on that date and time.' )

		#Check if student is not available
		stud_availability = g.g_sql.execqry("SELECT * FROM isStudAvailable('"+ str(self._m_id) +"', " + str(p_prof_sched_id) + ", '" + p_date + "')", False)
		if not f.is_none_list(stud_availability):
			raise Exception('You are not available on that date and time.' )

		appt_stored = g.g_sql.execqry("SELECT * FROM setappointment('" + str(p_prof_id)+ "', '" +
															str(self._m_id)+ "', " +
															str(p_prof_sched_id) + ", '" +
															p_date + "', '" +
															p_msg+ "')", True)

		if f.is_none_list(appt_stored):
			raise Exception('There was a problem sending your appointment request.')

		return {'prof_name' : prof.getFirstName() + ' ' + prof.getLastName()}