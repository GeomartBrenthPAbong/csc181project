----------------------------------	TABLES

-- @desc Defining composite types for student name and professor name

CREATE TYPE professor_name AS (
	prof_first_name VARCHAR(50),
	prof_last_name VARCHAR(50)
);

CREATE TYPE student_name AS (
	stud_first_name VARCHAR(50),
	stud_last_name VARCHAR(50)
);

-- @desc Creating SCHEDULE Table

CREATE TABLE pc_schedule(
	sched_id INT PRIMARY KEY,
    sched_from_time TIME,
    sched_to_time TIME,
    sched_day VARCHAR
);

-- @desc Creating PROFESSOR Table

CREATE TABLE pc_professor(
	prof_employment_id VARCHAR(20),
	prof_name professor_name,
	prof_email_add VARCHAR(80),
	prof_phone_number VARCHAR(20),
	sched_id INT REFERENCES pc_schedule(sched_id),
	PRIMARY KEY (prof_employment_id)
);

-- @desc Creating STUDENT Table

CREATE TABLE pc_student(
	 stud_id_number VARCHAR(10),
     stud_name student_name,
     stud_phone_number VARCHAR(15),
     stud_email VARCHAR(100),
	 stud_password VARCHAR(100),
	 PRIMARY KEY (stud_id_number)
);

-- @desc Creating APPOINTMENT Table

CREATE TABLE pc_appointment (
     appointment_id INT PRIMARY KEY,
	 state_viewed BOOLEAN,
	 prof_employment_id VARCHAR(20)REFERENCES pc_professor(prof_employment_id) UNIQUE,
	 student_id_number VARCHAR(10) REFERENCES pc_student(stud_id_number) UNIQUE,
	 schedule_id INT REFERENCES pc_schedule(sched_id) UNIQUE,
	 appointment_date DATE,
	 message TEXT
);

-- @desc Creating a table matching setting schedules for professors

CREATE TABLE pc_professor_sched(
	prof_sched_id INT PRIMARY KEY,
	prof_employment_id VARCHAR(20) REFERENCES pc_professor(prof_employment_id),
	sched_id INT REFERENCES pc_schedule(sched_id)
);


---------------------------------- PROFESSOR TABLE SCRIPT


-- @desc Use this function for storing new professor details or updating an existing professor details
-- @var p_prof_employment_id the professor employment id
-- @var p_first_name the first name
-- @var p_last_name the last name
-- @var p_email_add the email address
-- @var p_phone_number a Philippine specific phone number
-- @returns TEXT

CREATE OR REPLACE
	FUNCTION setProfessor(p_prof_employment_id VARCHAR,
						  p_prof_name professor_name,
                          p_email_add VARCHAR,
                          p_phone_number VARCHAR)
	RETURNS TEXT AS
	$$
		DECLARE
			v_professor_instance VARCHAR;
		BEGIN
		SELECT INTO v_professor_instance prof_email_add FROM pc_professor 
		WHERE prof_email_add = p_email_add;

		IF v_professor_instance ISNULL THEN
			INSERT INTO pc_professor(prof_employment_id, 
										prof_name, 
										prof_email_add, 
										prof_phone_number) 
			VALUES(p_prof_employment_id, 
					p_prof_name , 
					p_email_add, 
					p_phone_number);
		ELSE
			UPDATE pc_professor
			SET prof_employment_id = p_prof_employment_id,
				prof_first_name = p_first_name,
				prof_last_name = p_last_name,
				prof_phone_number = p_phone_number
			WHERE prof_email_add = p_email_add;
		END IF;
    RETURN 'OK';
	END;
	$$
 LANGUAGE 'plpgsql';

 CREATE OR REPLACE
	FUNCTION extractProfessorInfoPerEmail(IN p_email_add VARCHAR,
										  OUT prof_employment_id VARCHAR,
										  OUT name professor_name,
										  OUT email_address VARCHAR,
										  OUT phone_number VARCHAR)
	RETURNS SETOF RECORD AS
	$$
		SELECT 
			prof_employment_id,
			prof_name,
			prof_email_add,
			prof_phone_number
		FROM 
			pc_professor
		WHERE 
			prof_email_add = $1;
	$$
LANGUAGE 'sql';



---------------------------------- SCHEDULE TABLE SCRIPT


-- @desc Use this function to create a schedule. If the schedule already exists, the function does nothing
-- @var p_from_time
-- @var p_to_time
-- @var p_schedule_day
-- RETURNS TEXT

CREATE OR REPLACE
	FUNCTION createSchedule(p_schedule_id INT, p_from_time TIME, p_to_time TIME, p_schedule_day VARCHAR)
	RETURNS TEXT AS
	$$
		DECLARE
			v_schedule_instance INT;
		BEGIN
			SELECT INTO v_schedule_instance p_sched_id FROM pc_schedule
			WHERE sched_from_time = p_time_from 
			AND sched_to_time = p_to_time 
			AND sched_day = p_schedule_day ;

		IF v_schedule_instance ISNULL THEN
			INSERT INTO pc_schedule(sched_id, sched_from_time, sched_to_time, sched_day) 
			VALUES (p_schedule_id, p_from_time, p_to_time, p_schedule_day);
		END IF;
		RETURN 'OK';
		END;
	$$
LANGUAGE 'plpgsql';


-- @desc Use this function to edit an existing schedule.
-- @var p_schedule_id the id of the schedule
-- @var p_from_time the new from time
-- @var p_to_time the new to time
-- @var p_schedule_day the new schedule day

CREATE OR REPLACE
	FUNCTION editSchedule(p_schedule_id INT, p_from_time TIME, p_to_time TIME, p_schedule_day VARCHAR)
	RETURNS TEXT AS
	$$
	DECLARE
		v_schedule_instance INT;
	BEGIN
		SELECT INTO v_schedule_instance sched_id FROM pc_schedule
		WHERE sched_id = p_schedule_id;

		IF v_schedule_instance ISNULL THEN
			RETURN 'NO INSTANCE';
		ELSE
			UPDATE pc_schedule
				SET sched_from_time = p_from_time,
					sched_to_time = p_to_time,
					sched_day = p_schedule_day
				WHERE sched_id = p_schedule_id;
			RETURN 'OK';
		END IF;
	END;
	$$
LANGUAGE 'plpgsql';


-- @desc Use this function to get schedule information given the id
-- @var p_int_schedule the schedule id
-- @returns SETOF RECORD a list of time range
CREATE OR REPLACE
  FUNCTION extractScheduleInfoFromID(IN INT,
                                     OUT TIME,
                                     OUT TIME,
                                     OUT VARCHAR)
  RETURNS SETOF RECORD AS
  $$
    SELECT sched_from_time,
           sched_to_time,
           sched_day
    FROM pc_schedule
    WHERE sched_id = $1;
  $$
  LANGUAGE 'sql';
  
  ---------------------------------- STUDENT TABLE SCRIPT
  

-- @desc Use this function for storing new student details or updating an existing student details
-- @var p_student_id_number the PRIMARY key
-- @var p_student_name the student name
-- @var p_phone_number the student phone number (Philippines local number)
-- @var p_student_email the student email
-- @var p_student_pass the student pass

CREATE OR REPLACE 
    FUNCTION setobj1(p_student_id_number VARCHAR,
	                 p_student_name student_name, 
					 p_phone_number VARCHAR, 
					 p_student_email VARCHAR, 
					 p_student_pass VARCHAR) 
    RETURNS text AS
$$
  DECLARE
     v_student_id_number VARCHAR;
  BEGIN
      SELECT INTO v_student_id_number stud_id_number FROM pc_student
         WHERE stud_id_number = p_student_id_number;
         
      IF v_student_id ISNULL THEN
          INSERT INTO pc_student(stud_id_number,
		                       stud_name, 
							   stud_phone_number, 
							   stud_email, 
							   stud_pass) 
							   
					   VALUES (p_student_id_number,
							   p_student_name, 
							   p_phone_number, 
							   p_student_email, 
							   p_student_pass);
      ELSE
          UPDATE pc_student 
            SET stud_name = p_student_name
            WHERE stud_id_number = p_student_id_number;
      END IF;   
         
      RETURN 'OK';
  END;
$$
  LANGUAGE 'plpgsql'; 
  
-- @desc Use this function to view the created table
CREATE OR REPLACE FUNCTION 
    extractStudentInfoPerId(IN VARCHAR, OUT VARCHAR, OUT student_name, OUT VARCHAR, OUT VARCHAR, OUT VARCHAR) 
RETURNS setof RECORD AS
$$ 
     SELECT * FROM pc_student
     WHERE stud_id_number = $1;
     
$$
 LANGUAGE 'sql';

 
 
 ---------------------------------------------------------------------------------------------------------------------------------------
-- @desc Use this function for adding a schedule for a certain professor or updating the specific schedule of a certain professor
-- @var p_professor_id the unique id of the professor
-- @var p_schedule_id the unique id of the schedule
-- @returns TEXT

CREATE OR REPLACE
	FUNCTION addScheduleToProfessor(p_professor_employment_id VARCHAR,
									p_schedule_id INT)
	RETURNS TEXT AS
	$$
		DECLARE
			v_prof_employment_id VARCHAR;
			v_schedule_id INT;
		BEGIN
			SELECT INTO v_prof_employment_id,
						v_schedule_id prof_employment_id, 
						sched_id 
			FROM pc_professor_sched
			WHERE prof_employment_id = p_professor_employment_id AND 
				sched_id = p_schedule_id;

			IF v_prof_employment_id AND v_schedule_id ISNULL THEN
				INSERT INTO pc_professor_sched  (prof_employment_id, 
												sched_id) 
				VALUES(p_professor_employment_id, 
						p_schedule_id);
			ELSE						-- should put a warning here, in case prof tries to make a sched with existing entry
				UPDATE pc_professor_sched
				SET sched_id = p_schedule_id
				WHERE prof_employment_id = p_professor_employment_id;
			END IF;
			RETURN 'OK';
		END;
  $$
  LANGUAGE 'plpgsql';
  -------------------------------------------------------------------------------------------------------------------------------------------------------------
  
  
  -- @desc Use this function to get the schedules of a certain professor
-- @var p_professor_id is the professor id
-- @returns SETOF INT a list of schedule ids

CREATE OR REPLACE
	FUNCTION getSchedules(IN p_prof_employment_id VARCHAR,
						  OUT schedule_id INT)
	RETURNS SETOF INT AS
	$$
		SELECT 
			sched_id
		FROM 
			pc_professor_sched
		WHERE 
			prof_employment_id = $1;
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
							p_professor_id INT, 
							p_student_id INT, 
							p_schedule_id INT, 
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
									 professor_id, 
									 student_id, 
									 schedule_id, 
									 appointment_date, 
									 message) 
			VALUES (p_appointment_id, 
					p_state_viewed, 
					p_professor_id, 
					p_student_id, 
					p_schedule_id, 
					p_appointment_date, 
					p_message);
      ELSE
          UPDATE pc_appointment 
            SET state_viewed 		= p_state_viewed, 
				professor_id 		= p_professor_id,
				student_id 			= p_student_id,
				schedule_id 		= p_schedule_id,
				appointment_date 	= p_appointment_date,
				message 			= p_message
            WHERE appointment_id 	= p_appointment_id;
      END IF;   
         
      RETURN 'OK';
  END;
$$
	LANGUAGE 'plpgsql';
	
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

-- @desc Use this function to get list of appointments and details using unique professor id
-- @var p_professor_id is the professor id
-- @returns setof record a set of appointments and their details
CREATE OR REPLACE FUNCTION 
    getApptPerProfId(IN VARCHAR, 
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
     WHERE prof_employment_id = $1;
     
$$
 LANGUAGE 'sql';

 -- @desc Use this function to get list of appointments and details using unique student id
 -- @var p_student_id is the unique student id
 -- @returns setof record A set of appointments and their details
CREATE OR REPLACE FUNCTION
	getApptPerStudId(IN VARCHAR, 
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
	WHERE student_id_number = $1;
$$
LANGUAGE 'sql';

-- @desc Use this function to get appointment details using unique student id and professor id
-- @var p_student_id The unique student id
-- @var p_professor_id The unique professor id
-- @return setof record A set of appointment details
CREATE OR REPLACE FUNCTION
	getApptPerStudProfId(IN VARCHAR, 
					IN VARCHAR,
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
	WHERE student_id_number = $1 AND
	prof_employment_id = $2;
$$
LANGUAGE 'sql';€