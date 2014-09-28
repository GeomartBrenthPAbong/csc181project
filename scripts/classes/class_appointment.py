class Appointment(object):
	def __init__(self):
		self.__m_id = None
		self.__m_state_viewed = False
		self.__m_status = False
		self.__m_professor = None
		self.__m_student = None
		self.__m_schedule = None
		self.__m_appointment_date = None
		self.__m_appointment_msg = None

	##==============================
	## Getters and Setters

	def setID(self, p):
		self.__m_id = p

	def setStateViewed(self, p_state_viewed):
		self.__m_state_viewed = p_state_viewed

	def setStatus(self, p_status):
		self.__m_status = p_status

	def setProfessor(self, p_professor):
		self.__m_professor = p_professor

	def setStudent(self, p_student):
		self.__m_student = p_student

	def setSchedule(self, p_schedule):
		self.__m_schedule = p_schedule

	def setAppointmentDate(self, p_appointment_date):
		self.__m_appointment_date = p_appointment_date

	def setAppointmentMsg(self, p_appointment_msg):
		self.__m_appointment_msg = p_appointment_msg

	def getID(self):
		return self.__m_id

	def getStateViewed(self):
		return self.__m_state_viewed

	def getStatus(self):
		return self.__m_status

	def getProfessor(self):
		return self.__m_professor

	def getStudent(self):
		return self.__m_student

	def getSchedule(self):
		return self.__m_schedule

	def getAppointmentDate(self):
		return self.__m_appointment_date

	def getAppointmentMsg(self):
		return self.__m_appointment_msg

	##==============================
	## Other functions

	def changeStatus(self):
		g.g_sql.execqry("SELECT* FROM changeStatus(" + str(self.__m_id) + ", " + self.__m_status + ")", True)

	def changeStateViewed(self):
		g.g_sql.execqry("SELECT * FROM changeState(" + str(self.__m_id) + ", " + self.__m_status + ")", True)

	### Creates an object using the tuples passed
	###
	### @param string p_professor
	### @param string p_student
	### @param int p_schedule
	### @param date p_appointment_date
	### @param string p_appointment_msg
	### @return Appointment
	### @throws ENotEnoughDetails
	### @throws EInvalidFormat
	@staticmethod
	def createObject((p_professor,
						p_student,
						p_schedule,
						p_appointment_date,
						p_appointment_msg)):

		import scripts.exceptions.e_notenoughdetails as e_notenoughdetails

		if p_professor is None or \
			p_student is None or \
			p_schedule is None or \
			p_appointment_date is None or \
			p_appointment_msg is None:
				raise e_notenoughdetails.ENotEnoughDetails('All appointment details are required')

		import scripts.functions as functions
		import scripts.exceptions.e_invalidformat as e_invalidformat

		if not functions.is_date_format(p_appointment_date):
			raise e_invalidformat.EInvalidFormat('Invalid apppointment date')

		appointment = Appointment()
		appointment.setProfessor(p_professor)
		appointment.setStudent(p_student)
		appointment.setSchedule(p_schedule)
		appointment.setAppointmentDate(p_appointment_date)
		appointment.setAppointmentMsg(p_appointment_msg)

		return appointment

	### Creates Appointment object given an appointment ID
	###
	### @param int p_appointment_id
	### @return Appointment
	### @throws ENotRegistered
	@staticmethod
	def dbExtract(p_appointment_id):
		import scripts.global_variables as g
		import scripts.exceptions.e_notregistered as e_notregistered

		try:
			[(
				_,
				state_viewed,
				status,
				professor_id,
				student_id,
				schedule_id,
				appointment_date,
				appointment_msg
			)] = g.g_sql.execqry("SELECT * FROM getApptDetails('" + p_appointment_id + "')")
		except:
			raise e_notregistered.ENotRegistered('Appointment does not exists.')

		import scripts.classes.class_user_factory as user_factory
		import scripts.classes.class_schedule as schedule

		appointment = Appointment()
		appointment.setID(p_appointment_id)
		appointment.setStateViewed(state_viewed)
		appointment.setProfessor(user_factory.UserFactory().createUser(professor_id))
		appointment.setStudent(user_factory.UserFactory().createUser(student_id))
		appointment.setSchedule(schedule.Schedule().dbExtract(schedule_id))
		appointment.setAppointmentDate(appointment_date)
		appointment.setAppointmentMsg(appointment_msg)

		return appointment

	### Stores the appointment to the appointment table
	###
	### @throws ENotEnoughDetails
	### @throws EInvalidFormat
	### @throws EAlreadyExists
	def dbStore(self):
		import scripts.exceptions.e_notenoughdetails as e_notenoughdetails

		if self.__m_professor is None or \
			self.__m_student is None or \
			self.__m_schedule is None or \
			self.__m_appointment_date is None or \
			self.__m_appointment_msg is None:
				raise e_notenoughdetails.ENotEnoughDetails('All appointment details are required.')

		import scripts.functions as functions
		import scripts.exceptions.e_invalidformat as e_invalidformat

		if not functions.is_date_format(self.__m_appointment_date):
			raise e_invalidformat.EInvalidFormat('Invalid apppointment date')

		import scripts.exceptions.e_alreadyexists as e_exists

		if functions.appointment_exists(self.__m_professor.getID(), self.__m_student.getID):
			raise e_exists.EAlreadyExists('Appointment already exists.')

		import scripts.global_variables as g

		((self.__m_id,),) = g.g_sql.execqry("SELECT * FROM setAppointment(" + self.__m_state_viewed + ", " +
											self.__m_status + ", '" +
											self.__m_professor.getID() + "', '" +
											self.__m_student.getID() + "', " +
											str(self.__m_schedule.getID()) + ", " +
											self.__m_appointment_date + ", '" +
											self.__m_appointment_msg + "')", True)

