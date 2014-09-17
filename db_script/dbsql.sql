---------------TABLES

-- @desc Defining composite types for user names

CREATE TYPE full_name AS (
	first_name VARCHAR(50),
	last_name VARCHAR(50)
);

-- @desc Creating SCHEDULE Table

CREATE TABLE pc_schedule(
	sched_id INT PRIMARY KEY,
    sched_from_time TIME,
    sched_to_time TIME,
    sched_day VARCHAR
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
	phone_number VARCHAR(20),
	account_type VARCHAR REFERENCES pc_account_type(account_type) UNIQUE,
	password VARCHAR(100),
	PRIMARY KEY (user_id)
);

-- @desc Creating APPOINTMENT Table

CREATE TABLE pc_appointment (
     appointment_id INT PRIMARY KEY,
	 state_viewed BOOLEAN,
	 prof_id VARCHAR(20)REFERENCES pc_user(user_id) UNIQUE,
	 stud_id VARCHAR(20) REFERENCES pc_user(user_id) UNIQUE,
	 sched_id INT REFERENCES pc_schedule(sched_id) UNIQUE,
	 appointment_date DATE,
	 message TEXT
);

-- @desc Creating a table matching setting schedules for professors

CREATE TABLE pc_professor_schedule(
	prof_sched_id INT PRIMARY KEY,
	prof_id VARCHAR(20) REFERENCES pc_user(user_id),
	sched_id INT REFERENCES pc_schedule(sched_id)
);

---------------------------- USER TABLE SCRIPT

-- @desc Use this function to add user data

CREATE OR REPLACE
	FUNCTION setUser(p_user_id VARCHAR,
						  p_fuser_name full_name,
                          p_email_add VARCHAR,
                          p_phone_number VARCHAR,
						  p_account_type VARCHAR,
						  p_password VARCHAR)
	RETURNS TEXT AS
	$$
		DECLARE
			v_user_instance VARCHAR;
		BEGIN
		SELECT INTO v_user_instance email_add FROM pc_user
		WHERE email_add = p_email_add;

		IF v_user_instance ISNULL THEN
			INSERT INTO pc_user(user_id, 
								fuser_name, 
								email_add, 
								phone_number,
								account_type,
								password) 
			VALUES(p_user_id, 
					p_fuser_name, 
					p_email_add, 
					p_phone_number,
					p_account_type,
					p_password) ;
		ELSE
			UPDATE pc_user
			SET user_id = p_user_id,
				fuser_name = p_fuser_name,
				phone_number = p_phone_number,
				account_type = p_account_type,
				password = p_password
			WHERE email_add = p_email_add;
		END IF;
    RETURN 'OK';
	END;
	$$
 LANGUAGE 'plpgsql';
 
 -- @desc Function to extract user details per user id
 
  CREATE OR REPLACE
	FUNCTION extractUserDetailsPerId(IN VARCHAR,
								OUT VARCHAR,
								OUT full_name,
								OUT VARCHAR,
								OUT VARCHAR,
								OUT VARCHAR)
	RETURNS SETOF RECORD AS
	$$
		SELECT 
			user_id,
			fuser_name,
			email_add,
			phone_number,
			account_type
		FROM 
			pc_user
		WHERE 
			user_id = $1;
	$$
LANGUAGE 'sql';

---------------------------------- SCHEDULE TABLE SCRIPT


-- @desc Use this function to create a schedule. If the schedule already exists, the function does nothing
-- @var p_from_time
-- @var p_to_time
-- @var p_schedule_day
-- RETURNS TEXT

CREATE OR REPLACE
	FUNCTION createSchedule(
								p_from_time TIME, 
								p_to_time TIME
						   )
	RETURNS TEXT AS
	$$
		DECLARE
			v_sched_instance INT;
		BEGIN
			SELECT 
				INTO v_sched_instance sched_id 
				FROM pc_schedule
				WHERE sched_from_time = p_from_time
				AND sched_to_time = p_to_time 
				AND sched_day = p_sched_day ;

		IF v_sched_instance ISNULL THEN
			INSERT 
				INTO pc_schedule(
								 sched_id, 
								 sched_from_time, 
								 sched_to_time, 
								 sched_day
								) 
				VALUES (
					    p_sched_id, 
					    p_from_time, 
						p_to_time, 
						p_sched_day
					   );
			RETURN 'OK';
		ELSE RETURN 'Schedule already exists.';
		END IF;


	
	END;
	$$
LANGUAGE 'plpgsql';

-- @desc Function edits schedule table

CREATE OR REPLACE
	FUNCTION editSchedule(
						  p_sched_id INT, 
						  p_from_time TIME, 
						  p_to_time TIME, 
						 )
	RETURNS TEXT AS
	$$
	DECLARE
		v_sched_instance INT;
	BEGIN
		SELECT 
			INTO v_sched_instance sched_id 
			FROM pc_schedule
			WHERE sched_id = p_sched_id;

		IF v_sched_instance ISNULL THEN
			RETURN 'NO INSTANCE';
		ELSE
			UPDATE pc_schedule
				SET sched_from_time = p_from_time,
					sched_to_time = p_to_time,
					sched_day = p_sched_day
				WHERE sched_id = p_sched_id;
			RETURN 'OK';
		END IF;
	END;
	$$
LANGUAGE 'plpgsql';


-- @desc Use this function to get schedule information given the id
-- @var p_int_schedule the schedule id
-- @returns SETOF RECORD a list of time range

CREATE OR REPLACE
  FUNCTION extractScheduleInfoFromID(
									 IN INT,
                                     OUT TIME,
                                     OUT TIME,
                                     OUT VARCHAR
									)
  RETURNS SETOF RECORD AS
  $$
    SELECT sched_from_time,
           sched_to_time,
           sched_day
    FROM pc_schedule
    WHERE sched_id = $1;
  $$
  LANGUAGE 'sql';

-- @desc Use this function for adding a schedule for a certain professor or updating the specific schedule of a certain professor
-- @var p_professor_id the unique id of the professor
-- @var p_schedule_id the unique id of the schedule
-- @returns TEXT

CREATE OR REPLACE
	FUNCTION addScheduleToProfessor(p_prof_sched_id INT, p_prof_id VARCHAR,
									p_sched_id INT)
	RETURNS TEXT AS
	$$
		DECLARE
			v_prof_id VARCHAR;
			v_sched_id INT;
			v_account_type VARCHAR;
		BEGIN
			SELECT INTO v_account_type account_type FROM pc_user WHERE user_id = p_prof_id;
			IF v_account_type = 'Professor' THEN
				SELECT INTO v_prof_id, v_sched_id 
						prof_id, sched_id 
				FROM pc_professor_schedule
				WHERE prof_id = p_prof_id AND 
					sched_id = p_sched_id;

				IF v_prof_id ISNULL AND v_sched_id ISNULL THEN
					INSERT INTO pc_professor_schedule  (prof_sched_id, prof_id, 
											sched_id) 
						VALUES(p_prof_sched_id, p_prof_id, 
						p_sched_id);
					RETURN 'OK';
				ELSE RETURN 'Professor already has that schedule';	-- should put a warning here, in case prof tries to make a sched with existing entry
				END IF;
			ELSE RETURN 'Cannot add schedule to ''student'' type account';
			END IF;
		
		END;
  $$
  LANGUAGE 'plpgsql';
  
  CREATE OR REPLACE
	FUNCTION getProfessorSchedules(IN p_prof_id VARCHAR,
						  OUT sched_id INT)
	RETURNS SETOF INT AS
	$$
		SELECT 
			sched_id
		FROM 
			pc_professor_schedule
		WHERE 
			prof_id = $1;
	$$
LANGUAGE 'sql';

-----------------------------------APPOINTMENT TABLE SCRIPT

-- @desc Use this function to store new appointments or update existing appointment details
-- @var p_appointment_id the unique appointment id
-- @var p_state_viewed the viewed state of the appointment
-- @var p_student_id the student id from table pc_student
-- @var p_schedule_id the schedule id from table pc_schedule
-- @var p_appointment_date the date of the appointment
-- @var p_message the optional message along with the appointment
-- @returns text

CREATE OR REPLACE 
    FUNCTION newAppointment(p_appointment_id INT, 
							p_state_viewed BOOLEAN, 
							p_prof_id VARCHAR, 
							p_stud_id VARCHAR, 
							p_sched_id INT, 
							p_appointment_date DATE, 
							p_message TEXT) 
    RETURNS TEXT AS
$$
  DECLARE
     v_appointment_id INT;
  BEGIN
    SELECT INTO v_appointment_id appointment_id 
		FROM pc_appointment 
        WHERE appointment_id = p_appointment_id;
         
      IF v_appointment_id ISNULL THEN
          INSERT INTO pc_appointment(appointment_id, 
									 state_viewed, 
									 prof_id, 
									 stud_id, 
									 sched_id, 
									 appointment_date, 
									 message) 
			VALUES (p_appointment_id, 
					p_state_viewed, 
					p_prof_id, 
					p_stud_id, 
					p_sched_id, 
					p_appointment_date, 
					p_message);
      ELSE
          UPDATE pc_appointment 
            SET state_viewed 		= p_state_viewed, 
				prof_id 		= p_prof_id,
				stud_id 			= p_stud_id,
				sched_id 			= p_sched_id,
				appointment_date 	= p_appointment_date,
				message 			= p_message
            WHERE appointment_id 	= p_appointment_id;
      END IF;   
         
      RETURN 'OK';
  END;
$$
	LANGUAGE 'plpgsql';
----------------------------------------------------------------------------------	
-- @desc Use this function to change the viewed state of the appointment
-- @var p_appointment_id The unique appointment id
-- @returns text
CREATE OR REPLACE FUNCTION
	changeState(p_appointment_id INT)
	RETURNS TEXT AS
$$
	DECLARE
		v_appointment_id INT;
		v_state_viewed BOOLEAN;
	BEGIN
		SELECT INTO v_appointment_id appointment_id 
			FROM pc_appointment 
			WHERE appointment_id = p_appointment_id;
			
		SELECT INTO v_state_viewed state_viewed 
			FROM pc_appointment 
			WHERE appointment_id = p_appointment_id;
			
		IF v_appointment_id ISNULL THEN
			RETURN 'Appointment no longer exists.';
			
		ELSE
			IF v_state_viewed THEN
				RETURN 'Appointment already viewed!';
				
			ELSE
				UPDATE pc_appointment
					SET state_viewed = TRUE
					WHERE appointment_id = p_appointment_id;
			END IF;
		END IF;
		RETURN 'OK';
		
	END;
$$
  LANGUAGE 'plpgsql'; 
  
-- @desc Use this function to delete existing appointments
-- @var p_appointment_id The unique appointment id
-- @returns text
CREATE OR REPLACE FUNCTION
	deleteAppt(p_appointment_id INT)
	RETURNS TEXT AS
$$
	DECLARE
		v_appointment_id INT;
	BEGIN
		SELECT INTO v_appointment_id appointment_id 
			FROM pc_appointment 
			WHERE appointment_id = p_appointment_id;
		
		IF v_appointment_id ISNULL THEN
			RETURN 'The appointment you are trying to remove does not exist.';
		ELSE
			DELETE FROM pc_appointment
				WHERE appointment_id = p_appointment_id;
				RETURN 'Appointment deleted';
		END IF;
		RETURN 'OK';
		
	END;
$$
  LANGUAGE 'plpgsql'; 

--view

-- @desc Use this function to get list of appointments and details using unique user id
-- @returns setof record a set of appointments and their details

CREATE OR REPLACE FUNCTION 
    getApptPerId(IN VARCHAR, 
					OUT INT, 
					OUT BOOLEAN, 
					OUT VARCHAR, 
					OUT VARCHAR, 
					OUT INT, 
					OUT DATE, 
					OUT TEXT) 
RETURNS setof RECORD AS
$$ 
     SELECT * FROM pc_appointment
     WHERE prof_id = $1 OR stud_id = $1;
     
$$
 LANGUAGE 'sql';

-- @desc Use this function to check existence of record

CREATE OR REPLACE FUNCTION
	checkExistence(IN VARCHAR,
					OUT VARCHAR,
					OUT VARCHAR)
RETURNS setof RECORD AS
$$
	SELECT user_id, account_type FROM pc_user
	WHERE user_id = $1;
$$
LANGUAGE 'sql';