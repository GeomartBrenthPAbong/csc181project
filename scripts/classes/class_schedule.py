import class_dosql as sql

class Schedule(object):

	__m_sql = sql.doSql()

	def __init__ (self):
		self.__m_id = None
		self.__m_from_time = None
		self.__m_to_time = None
		self.__m_query = None

	def setFromTime(self, p_from_time):
		self.__m_from_time = p_from_time

	def setToTime(self, p_to_time):
		self.__m_to_time = p_to_time

	@staticmethod
	def createObject((p_from_time, p_to_time, p_sched_day)):
		schedule = Schedule()
		schedule.setFromTime(p_from_time)
		schedule.setToTime(p_to_time)
		return schedule

	def dbStore(self):
		self.__m_query = "createSchedule( "
		self.__m_query += self.__m_from_time + ","
		self.__m_query += self.__m_to_time + ")"
		[self.__m_id] = __m_sql.execqry(self.__m_query, True)
		#provided that createScheule in dbsql should return us
		#the id of this schedule 

	@staticmethod
	def editSchedule((p_sched_id, p_new_from_time, p_new_to_time)):
		self.__m_query = "checkSchedExistence( " + str(p_sched_id) + ")"
		[self.__m_id] = __m_sql.execqry(self.__m_query, False)
		
		#if p_sched_id is existing







		
		 
