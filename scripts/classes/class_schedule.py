class Schedule(object):
	def __init__ (self):
		self.__m_id = None
		self.__m_from_time = None
		self.__m_to_time = None

	##==============================
	## Getters and Setters

	def setID(self, p_id):
		self.__m_id = p_id

	def setFromTime(self, p_from_time):
		self.__m_from_time = p_from_time

	def setToTime(self, p_to_time):
		self.__m_to_time = p_to_time

	def getID(self):
		return self.__m_id

	def getFromTime(self):
		return self.__m_from_time

	def getToTime(self):
		return self.__m_to_time

	##==============================
	## Other functions

	### Creates a Schedule object using time
	###
	### @param string p_from_time
	### @param string p_to_time
	### @return Schedule
	### @throws ENotEnoughDetails
	### @throws EInvalidFormat
	@staticmethod
	def createObject((p_from_time, p_to_time)):
		import scripts.exceptions.e_notenoughdetails as e_notenoughdetails

		if p_from_time is None or \
			p_to_time is None:
				raise e_notenoughdetails.ENotEnoughDetails('From time and to time are required.')

		import scripts.functions as functions
		import scripts.exceptions.e_invalidformat as e_invalidformat

		if not functions.is_time_format(p_from_time):
			raise e_invalidformat.EInvalidFormat('From time is invalid.')

		if not functions.is_time_format(p_to_time):
			raise e_invalidformat.EInvalidFormat('To time is invalid.')

		schedule = Schedule()
		schedule.setFromTime(p_from_time)
		schedule.setToTime(p_to_time)
		return schedule

	### Creates a Schedule object using an id
	###
	### @param int p_schedule_id
	### @return Schedule
	### @throws ENotRegistered
	@staticmethod
	def dbExtract(p_schedule_id):
		import scripts.global_variables as g
		import scripts.exceptions.e_notregistered as e_notregistered

		try:
			[(
				_,
				from_time,
				to_time
			)] = g.g_sql.execqry('extractSchedInfoFromSchedID(' + p_schedule_id + ')')

			schedule = Schedule()
			schedule.setID(p_schedule_id)
			schedule.setFromTime(from_time)
			schedule.setToTime(to_time)

			return schedule
		except:
			raise e_notregistered.ENotRegistered('Schedule does not exists.')

	### Stores the schedule to the schedule table
	###
	### @throws ENotEnoughDetails
	### @throws EInvalidFormat
	### @throws EAlreadyExists
	def dbStore(self):
		import scripts.exceptions.e_notenoughdetails as e_notenoughdetails

		if self.__m_from_time is None or \
			self.__m_to_time is None:
				raise e_notenoughdetails.ENotEnoughDetails('All schedule details are required.')

		import scripts.functions as functions
		import scripts.exceptions.e_invalidformat as e_invalidformat

		if not functions.is_time_format(self.__m_from_time):
			raise e_invalidformat.EInvalidFormat('From time is invalid.')

		if not functions.is_time_format(self.__m_to_time):
			raise e_invalidformat.EInvalidFormat('To time is invalid.')

		import scripts.global_variables as g
		import scripts.exceptions.e_alreadyexists as e_alreadyexists

		if functions.schedule_time_exists(self.__m_from_time, self.__m_to_time):
			raise e_alreadyexists.EAlreadyExists('Schedule already exists.')

		((self.__m_id,),) = g.g_sql.execqry("SELECT * FROM setSchedule('" + self.__m_from_time + "', '" + self.__m_to_time + "')", True)
