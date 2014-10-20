class Appointment(object):
	def __init__(self):
		self.__m_id = None
		self.__m_state_viewed = False
		self.__m_status = False
		self.__m_professor = None
		self.__m_student = None
		self.__m_prof_sched_id = None
		self.__m_appointment_date = None
		self.__m_appointment_msg = None
		self.__m_sms = None

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

	def setProfSchedule(self, p_schedule):
		self.__m_prof_sched_id = p_schedule

	def setAppointmentDate(self, p_appointment_date):
		self.__m_appointment_date = p_appointment_date

	def setAppointmentMsg(self, p_appointment_msg):
		self.__m_appointment_msg = p_appointment_msg

	def setSMS(self, p_sms):
		self.__m_sms = p_sms

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

	def getProfSchedule(self):
		return self.__m_prof_sched_id

	def getAppointmentDate(self):
		return self.__m_appointment_date

	def getAppointmentMsg(self):
		return self.__m_appointment_msg

	def getSMS(self):
		return self.__m_sms

	##==============================
	## Other functions

	def changeStatus(self):
		import scripts.global_variables as g

		g.g_sql.execqry("SELECT* FROM changeStatus(" + str(self.__m_id) + ", '" + self.__m_status + "')", True)

	def changeStateViewed(self):
		import scripts.global_variables as g

		g.g_sql.execqry("SELECT * FROM changeState(" + str(self.__m_id) + ", '" + str(self.__m_state_viewed) + "')", True)

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
						p_prof_schedule,
						p_appointment_date,
						p_appointment_msg)):

		import scripts.exceptions.e_notenoughdetails as e_notenoughdetails

		if p_professor is None or \
			p_student is None or \
			p_prof_schedule is None or \
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
		appointment.setProfSchedule(p_prof_schedule)
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
				prof_sched_id,
				appointment_date,
				appointment_msg,
			    sms
			)] = g.g_sql.execqry("SELECT * FROM getapptdetails(" + str(p_appointment_id) + ")", False)

			import scripts.classes.class_user_factory as user_factory

			appointment = Appointment()
			appointment.setID(p_appointment_id)
			appointment.setStateViewed(state_viewed)
			appointment.setStatus(status)
			appointment.setProfessor(user_factory.UserFactory().createUserFromID(professor_id))
			appointment.setStudent(user_factory.UserFactory().createUserFromID(student_id))

			prof = appointment.getProfessor()
			appointment.setProfSchedule(prof.getSchedule(prof_sched_id))
			appointment.setAppointmentDate(str(appointment_date))
			appointment.setAppointmentMsg(appointment_msg)

			return appointment
		except:
			raise e_notregistered.ENotRegistered('Appointment does not exists.')

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
											str(self.__m_prof_sched_id) + ", " +
											self.__m_appointment_date + ", '" +
											self.__m_appointment_msg + "')", True)

