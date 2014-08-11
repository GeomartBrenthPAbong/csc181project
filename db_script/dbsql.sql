---------------------------------- PROFESSOR TABLE SCRIPT

-- @desc Use this function for storing new professor details or updating an existing professor details
-- @var p_str_first_name the first name
-- @var p_str_last_name the last name
-- @var p_str_email_address the email address
-- @var p_pn_phone_number a philippine specific phone number
-- @returns TEXT

CREATE OR REPLACE
  FUNCTION setProfessor(p_str_first_name VARCHAR,
                        p_str_last_name VARCHAR,
                        p_str_email_address VARCHAR,
                        p_pn_phone_number VARCHAR)
  RETURNS TEXT AS
  $$
  DECLARE
    v_professor_instance;
  BEGIN
    SELECT INTO v_professor_instance email_address FROM pc_professor WHERE email_address = p_str_email_address;

    IF v_professor_instance ISNULL THEN
      INSERT INTO pc_professor(first_name, last_name, email_address, phone_number) VALUES
                              (p_str_first_name, p_str_last_name, p_str_email_address, p_int_schedule_id, p_pn_phone_number);
    ELSE
      UPDATE pc_professor
        SET first_name = p_str_first_name,
            last_name = p_str_last_name,
            phone_number = p_pn_phone_number
        WHERE email_address = p_str_email_address
    END IF;
    RETURN 'OK';
  END;
  $$
  LANGUAGE 'plpgsql';

-- @desc Use this function for adding a schedule for a certain professor or updating the specific schedule of a certain professor
-- @var p_int_professor_id the unique id of the professor
-- @var p_int_schedule_id the unique id of the schedule
-- @returns TEXT
CREATE OR REPLACE
  FUNCTION addScheduleToProfessor(p_int_professor_id INT,
                       p_int_schedule_id INT)
  RETURNS TEXT AS
  $$
  DECLARE
    v_prof_sched_instance
  BEGIN
    SELECT INTO v_prof_sched_instance professor_id FROM pc_professor_schedule
      WHERE professor_id = p_int_professor_id AND schedule_id = p_int_schedule_id;

    IF v_prof_sched_instance ISNULL THEN
      INSERT INTO pc_professor_schedule(professor_id, schedule_id) VALUES
                                       (p_int_professor_id, p_int_schedule_id);
    ELSE
      UPDATE pc_professor_schedule
        SET schedule_id = p_int_schedule_id
        WHERE professor_id = p_int_schedule_id
    END IF;
    RETURN 'OK';
  END;
  $$
  LANGUAGE 'plpgsql';

-- @desc Use this function to extract information of a certain professor
-- @var p_str_email_address is the email address of the professor
-- @returns SETOF RECORD a set of professor details except the schedule
CREATE OR REPLACE
  FUNCTION extractProfessorInfoPerEmail(IN p_str_email_address,
                               OUT id INT,
                               OUT first_name VARCHAR,
                               OUT last_name VARCHAR,
                               OUT email_address VARCHAR,
                               OUT phone_number VARCHAR)
  RETURNS SETOF RECORD AS
  $$
    SELECT id,
           first_name,
           last_name,
           email_address,
           phone_number
    FROM pc_professor
    WHERE email_address = p_str_email_address
  $$
  LANGUAGE 'sql';

-- @desc Use this function to get the schedules of a certain professor
-- @var p_int_professor_id is the professor id
-- @returns SETOF INT a list of schedule ids
CREATE OR REPLACE
  FUNCTION getSchedules(IN p_int_professor_id INT,
                        OUT schedule_id INT)
  RETURNS SETOF INT AS
  $$
    SELECT schedule_id
    FROM pc_professor_schedule
    WHERE professor_id = p_int_professor_id
  $$
  LANGUAGE 'sql';

---------------------------------- SCHEDULE TABLE SCRIPT

-- @desc Use this function to get schedule information given the id
-- @var p_int_schedule the schedule id
-- @returns SETOF RECORD a list of time range
CREATE OR REPLACE
  FUNCTION extractScheduleInfoFromID(IN p_int_schedule_id INT,
                                     OUT from_time TIME,
                                     OUT to_time TIME)
  RETURNS SETOF RECORD AS
  $$
    SELECT from_time,
           to_time
    FROM pc_schedule
    WHERE id = p_int_schedule_id
  $$
  LANGUAGE 'sql';

-- @desc Use this function to create a schedule. If the schedule already exists, the function does nothing
-- @var p_time_from
-- @var p_time_to
-- RETURNS TEXT
CREATE OR REPLACE
  FUNCTION createSchedule(p_time_from TIME, p_time_to TIME)
  RETURNS TEXT AS
  $$
  DECLARE
    v_schedule_instance
  BEGIN
    SELECT INTO v_schedule_instance id FROM pc_schedule WHERE from_time = p_time_from AND to_time = p_time_to;

    IF v_schedule_instance ISNULL THEN
      INSERT INTO pc_schedule(from_time, to_time) VALUES
                             (p_time_from, p_time_to);
    END IF;
    RETURN 'OK';
  END;
  $$
  LANGUAGE 'plpgsql';

-- @desc Use this function to edit an existing schedule.
-- @var p_int_schedule_id the id of the schedule
-- @var p_time_from the new from time
-- @var p_time_to the new to time
CREATE OR REPLACE
  FUNCTION editSchedule(p_int_schedule_id INT, p_time_from TIME, p_time_to TIME)
  RETURNS TEXT AS
  $$
  DECLARE
    v_schedule_instance
  BEGIN
    SELECT INTO v_schedule_instance id FROM pc_schedule WHERE id = p_int_schedule_id;

    IF v_schedule_instance ISNULL THEN
      RETURN 'NO INSTANCE';
    ELSE
      UPDATE pc_schedule
      SET from_time = p_time_from,
          to_time = p_time_to
      WHERE id = p_int_schedule_id
      RETURN 'OK'
    END IF;
  END;
  $$
  LANGUAGE 'plpgsql';