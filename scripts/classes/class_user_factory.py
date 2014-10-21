class UserFactory():

	### Function that creates a Professor or Student object given a username and a password
	###
	### @param string p_usermame
	### @param string p_password
	### @return Professor|Student
	### @throw ENotRegistered
	@staticmethod
	def createUserFromUname(p_username, p_password):
		import scripts.exceptions.e_notregistered as error
		import scripts.global_variables as g

		try:
			((
				user_id,
				_
			),) = g.g_sql.execqry("SELECT * FROM checkAccountExistence('" + p_username + "', '" + p_password + "')", False)
		except:
			raise error.ENotRegistered('User does not exist or you entered an invalid credential.')
		return UserFactory().createUserFromID(user_id)

	### Function that creates a Professor or Student object given an ID
	###
	### @param string p_user_id is the user id
	### @return Professor|Student
	### @throw ENotRegistered
	@staticmethod
	def createUserFromID(p_user_id):
		import class_professor as professor
		import class_student as student
		import scripts.exceptions.e_notregistered as error
		import scripts.global_variables as g
		import scripts.functions as f

		try:
			((
				_,
				first_name,
				last_name,
				college,
				department,
				email_address,
				address,
				phone_number,
				account_type
			),) = g.g_sql.execqry("SELECT * FROM extractUserDetailsPerId('" + str(p_user_id) + "')", False)

			if account_type == 'Professor':
				user = professor.Professor()
			else:
				user = student.Student()
				list = g.g_sql.execqry("SELECT * FROM getUserMeta('"+str(p_user_id)+"', 'Course')", False)

				if not f.is_none_list(list):
					user.setCourse(list[0][0])

			user.setID(p_user_id)
			user.setFirstName(first_name)
			user.setLastName(last_name)
			user.setCollege(college)
			user.setDepartment(department)
			user.setEmailAddress(email_address)
			user.setAddress(address)
			user.setPhoneNumber(phone_number)
			user.setType(account_type)

			return user
		except:
			raise error.ENotRegistered('User does not exist.')