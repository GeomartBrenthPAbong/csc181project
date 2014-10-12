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
		return g.g_sql.execqry("SELECT * FROM getSchedIDPerProfID('" + self._m_id + "')", False)

	def addSchedule(self, p_schedule, p_day):
		((sched_id,),) = g.g_sql.execqry("SELECT * FROM addScheduleToProfessor('" +
										 self._m_id + "', " +
										 str(p_schedule.getID()) + ", '" +
										 p_day + "')", True)
		return sched_id

	def deleteSchedule(self, p_schedule):
		if p_schedule is None:
			return False

		g.g_sql.execqry("SELECT * FROM deleteProfSched('" +
						self._m_id + "', " +
						str(p_schedule.getID()) + ")", True)
		return True

	def editSchedule(self, p_old_schedule, p_new_schedule):
		if p_old_schedule is None or p_new_schedule is None:
			return False

		g.g_sql.execqry("SELECT * FROM editProfessorSchedule(" +
						str(p_old_schedule.getID()) + ", " +
						str(p_new_schedule.getID()) + ", '" +
						self._m_id + "')", False)
		return True

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