import class_user as user
import scripts.global_variables as g


class Professor(user.User):
	def __init__(self):
		self._m_type = 'professor'

	def getScheduleDay(self, p_schedule):
		((sched_day,),) = g.g_sql.execqry("SELECT * FROM getSchedDay('" + self._m_id + "', " +
										str(p_schedule.getID()) + ")", False)
		return sched_day

	def getSchedules(self):
		list = g.g_sql.execqry("SELECT * FROM getscheddetailsperprofid('" + self._m_id + "')", False)

		if len(list) is 1 and len(list[0]) is 1 and list[0][0] is 'None':
			return []
		else:
			return list

	def getArrangedSchedules(self):
		import class_schedule as s
		import scripts.exceptions.e_notregistered as en
		schedules = self.getSchedules()

		arranged_sched = {'mon': [], 'tue': [], 'wed': [], 'thu': [], 'fri': [], 'sat': [], 'sun': []}

		if len(schedules) is 0:
			return arranged_sched

		for (prof_sched, sched_id,day) in schedules:
			try:
				schedule = s.Schedule().dbExtract(sched_id)
			except en.ENotRegistered:
				continue
			arranged_sched[day].append([prof_sched, schedule])

	def addSchedule(self, p_schedule, p_day):
		((sched_id,),) = g.g_sql.execqry("SELECT * FROM addScheduleToProfessor('" +
										 self._m_id + "', " +
										 str(p_schedule.getID()) + ", '" +
										 p_day + "')", True)

		if sched_id == -1:
			import scripts.exceptions.e_nopermission as en
			raise en.ENoPermission('Students are not allowed to add schedules.')

		return sched_id

	def deleteSchedule(self, p_schedule):
		if p_schedule is None:
			return False

		g.g_sql.execqry("SELECT * FROM deleteProfSched('" +
						self._m_id + "', " +
						str(p_schedule.getID()) + ")", True)
		return True

	def editSchedule(self, p_prof_sched_id, p_new_schedule, p_new_day):
		if p_prof_sched_id is None or p_new_schedule is None or p_new_day is None:
			return False

		((state),) = g.g_sql.execqry("SELECT * FROM editProfessorSchedule(" +
						str(p_prof_sched_id) + ", " +
						str(p_new_schedule.getID()) + ", '" +
						p_new_day + "', '" +
						self._m_id + "')", True)
		return state

	def declineAppointment(self, p_appointment):
		if p_appointment is None:
			return False

		g.g_sql.execqry("SELECT * FROM deleteAppt(" + str(p_appointment.getID()) + ")", False)
		return True

	def getSchedule(self, p_prof_sched_id):
		try:
			((
				_,
				sched_id,
				_
			),) = g.g_sql.execqry("SELECT * FROM getProfSchedDetails(" + str(p_prof_sched_id) + ")",False)

			import scripts.classes.class_schedule as cs
			schedule = cs.Schedule().dbExtract(sched_id)
			return schedule
		except:
			import scripts.exceptions.e_notregistered as en
			raise en.ENotRegistered('Schedule does not exist!')

	def scheduleInUse(self, p_prof_sched_id):
		import scripts.functions as f

		return not f.is_none_list(g.g_sql.execqry("SELECT * FROM checkScheduleUsage('" + self._m_id + "'," + str(p_prof_sched_id) +")", False))

