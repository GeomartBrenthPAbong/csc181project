---------------TABLES

CREATE SEQUENCE appt_id_gen START 1 INCREMENT BY 1;
CREATE SEQUENCE prof_sched_id_gen START 1 INCREMENT BY 1;
CREATE SEQUENCE sched_id_gen START 1 INCREMENT BY 1;

-- @desc Defining composite types for user names

CREATE TYPE full_name AS (
	first_name VARCHAR(50),
	last_name VARCHAR(50)
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
	account_type VARCHAR(20) PRIMARY KEY
);

-- @desc Creating USER Table

CREATE TABLE pc_user(
	user_id VARCHAR(20),
	fuser_name full_name,
	email_add VARCHAR(80),
	address VARCHAR(80),
	phone_number VARCHAR(20),
	account_type VARCHAR REFERENCES pc_account_type(account_type),
	password VARCHAR(100),
	PRIMARY KEY (user_id)
);

-- @desc Creating APPOINTMENT Table

CREATE TABLE pc_appointment (
     appointment_id INT DEFAULT NEXTVAL('appt_id_gen'),
	 state_viewed BOOLEAN,
	 status BOOLEAN,
	 prof_id VARCHAR(20)REFERENCES pc_user(user_id) UNIQUE,
	 stud_id VARCHAR(20) REFERENCES pc_user(user_id) UNIQUE,
	 sched_id INT REFERENCES pc_schedule(sched_id) UNIQUE,
	 appointment_date DATE,
	 message TEXT,
	 PRIMARY KEY (appointment_id)
);
-- @desc Creating a table matching setting schedules for professors

CREATE TABLE pc_professor_schedule(
	prof_sched_id INT PRIMARY KEY DEFAULT NEXTVAL('prof_sched_id_gen'),
	prof_id VARCHAR(20) REFERENCES pc_user(user_id),
	sched_id INT REFERENCES pc_schedule(sched_id),
	sched_day VARCHAR(10)
);

CREATE TABLE pc_user_meta(
	user_id VARCHAR REFERENCES pc_user(user_id),
	meta_key VARCHAR(30),
	meta_value VARCHAR(50),
	PRIMARY KEY (user_id)
);
ALTER SEQUENCE appt_id_gen OWNED BY pc_appointment.appointment_id;
ALTER SEQUENCE prof_sched_id_gen OWNED BY pc_professor_schedule.prof_sched_id;
ALTER SEQUENCE sched_id_gen OWNED BY pc_schedule.sched_id;