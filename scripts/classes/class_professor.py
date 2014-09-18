import class_user as user
import scripts.global_variables as g


class Professor(user.User):
	def getSchedules(self):
		return g.g_sql.execqry('extractSchedIDInfoFromProfID(' + self._m_id + ')')

	def addSchedule(self, p_schedule):
		g.g_sql.execqry('addScheduleToProfessor(' + self._m_id + ', ' + p_schedule.getScheduleID() + ')')

	def editSchedule(self, p_old_schedule, p_new_schedule):
		if p_old_schedule is None or p_new_schedule is None:
			return False

		g.g_sql.execqry('editProfessorSchedule(' + p_old_schedule.getScheduleID() + ', ' + p_old_schedule.getScheduleID() + ')')
		return True

	def declineAppointment(self, p_appointment):
		if p_appointment is None:
			return False

		g.g_sql.execqry('deleteAppt(' + p_appointment.getAppointmentID() + ')')
		return True



