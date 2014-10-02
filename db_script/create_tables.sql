---------------TABLES

CREATE SEQUENCE appt_id_gen START 1 INCREMENT BY 1;
CREATE SEQUENCE prof_sched_id_gen START 1 INCREMENT BY 1;
CREATE SEQUENCE sched_id_gen START 1 INCREMENT BY 1;

-- @desc Defining composite types for user names

CREATE TYPE full_name AS (
	first_name TEXT,
	last_name TEXT
);

-- @desc Creating SCHEDULE Table

CREATE TABLE pc_schedule(
	sched_id INT DEFAULT NEXTVAL('sched_id_gen'),
	sched_from_time TIME,
	sched_to_time TIME,
	PRIMARY KEY (sched_id)
);

-- @desc Creating ACCOUNT TYPE Table

CREATE TABLE pc_account_type(
	account_type TEXT PRIMARY KEY
);

CREATE TABLE pc_status(
  status TEXT PRIMARY KEY
);

-- @desc Creating USER Table

CREATE TABLE pc_user(
	user_id TEXT,
	fuser_name full_name,
	college TEXT,
	department TEXT,
	email_add TEXT,
	address TEXT,
	phone_number TEXT,
	account_type TEXT REFERENCES pc_account_type(account_type),
	password TEXT,
	PRIMARY KEY (user_id)
);

-- @desc Creating APPOINTMENT Table

CREATE TABLE pc_appointment (
     appointment_id INT DEFAULT NEXTVAL('appt_id_gen'),
	 state_viewed BOOLEAN,
	 status TEXT REFERENCES pc_status(status),
	 prof_id TEXT REFERENCES pc_user(user_id),
	 stud_id TEXT REFERENCES pc_user(user_id),
	 sched_id INT REFERENCES pc_schedule(sched_id),
	 appointment_date DATE,
	 message TEXT,
	 PRIMARY KEY (appointment_id)
);
-- @desc Creating a table matching setting schedules for professors

CREATE TABLE pc_professor_schedule(
	prof_sched_id INT PRIMARY KEY DEFAULT NEXTVAL('prof_sched_id_gen'),
	prof_id TEXT REFERENCES pc_user(user_id),
	sched_id INT REFERENCES pc_schedule(sched_id),
	sched_day TEXT
);

CREATE TABLE pc_user_meta(
	user_id TEXT REFERENCES pc_user(user_id),
	meta_key TEXT,
	meta_value TEXT,
	PRIMARY KEY (user_id)
);
ALTER SEQUENCE appt_id_gen OWNED BY pc_appointment.appointment_id;
ALTER SEQUENCE prof_sched_id_gen OWNED BY pc_professor_schedule.prof_sched_id;
ALTER SEQUENCE sched_id_gen OWNED BY pc_schedule.sched_id;

-- @desc Creating session table
CREATE TABLE pc_session(
session_id TEXT,
user_id TEXT REFERENCES pc_user(user_id),
timestamp timestamp NOT NULL DEFAULT NOW(),
PRIMARY KEY (session_id)
);