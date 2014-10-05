INSERT INTO pc_account_type VALUES ('Student');
INSERT INTO pc_account_type VALUES ('Professor');

INSERT INTO pc_status VALUES ('Confirmed');
INSERT INTO pc_status VALUES ('Pending');
INSERT INTO pc_status VALUES ('Declined');

SELECT * FROM setSchedule ('07:00:00','07:30:00');
SELECT * FROM setSchedule ('07:30:00','08:00:00');
SELECT * FROM setSchedule ('08:00:00','08:30:00');
SELECT * FROM setSchedule ('08:30:00','09:00:00');

SELECT * FROM setUser ('2009-0207', row('Stephanie','Visitacion'), 'COE','EECE','teepanot7384@gmail.com', 'Sta. Cruz, Ozamiz City', '09207278184', 'Student', 'password');
SELECT * FROM setUser ('2009-7390', row('Carmelyn','Bernal'), 'COE','EECE','dramaPrincess1097@gmail.com', 'Brgy. Upper Hinaplanon, Iligan City', '09752150593', 'Student', 'password');
SELECT * FROM setUser ('2009-0731', row('Christopher Clint','Pacillos'), 'COE','EECE','buhatbuhatilangtep@gmail.com', 'Tibanga, Iligan City', '09104056412', 'Student', 'password');
SELECT * FROM setUser ('2011-1697', row('Janssen James','Tesaluna'), 'SCS','CS','janssen_snow@gmail.com', 'Brgy. Upper Hinaplanon, Iligan City', '09478392098', 'Student', 'password');
SELECT * FROM setUser ('2008-0886', row('Geomart Brenth','Abong'), 'COE','EECE','geomart_brenth@gmail.com', 'Tibanga, Iligan City', '09355678184', 'Student', 'password');
SELECT * FROM setUser ('2009-1133', row('Jimmy','Unilongo'), 'COE','EECE','jimtot@gmail.com', 'Tibanga, Iligan City', '09355671184', 'Student', 'password');
SELECT * FROM setUser ('2009-0040', row('Margie','Arda'), 'COE','EECE','marjie_yua@gmail.com', 'Tibanga, Iligan City', '09353678184', 'Student', 'password');
SELECT * FROM setUser ('2009-1284', row('Christian Nicole','Amil'), 'COE','EECE','christian_nicole@gmail.com', 'Tibanga, Iligan City', '09355675684', 'Student', 'password');
SELECT * FROM setUser ('2009-0567', row('Kim Chesed','Paller'), 'COE','EECE','kimchesed@gmail.com', 'Tibanga, Iligan City', '09355674584', 'Student', 'password');
SELECT * FROM setUser ('2009-7389', row('Sharyl','Calibayan'), 'COE','EECE','shrace_cal@gmail.com', 'Tibanga, Iligan City', '09355672345', 'Student', 'password');

SELECT * FROM setUser ('09-039', row('Orven','Llantos'), 'SCS','CS','submit.proj2oel@gmail.com', 'Iligan City', '09364534754', 'Professor', 'password');
SELECT * FROM setUser ('09-038', row('Kister Genesis','Jimenez'), 'COE','EECE','kister_genesis@gmail.com', 'Iligan City', '09364568734', 'Professor', 'password');
SELECT * FROM setUser ('09-037', row('Arnel','Zamayla'), 'COE','EECE','adzam@gmail.com', 'Iligan City', '09364348734', 'Professor', 'password');
SELECT * FROM setUser ('09-036', row('Rey','Lagrada'), 'COE','EECE','rey.lagrada@gmail.com', 'Iligan City', '09364568734', 'Professor', 'password');
SELECT * FROM setUser ('09-035', row('Mercedenia','Lambino'), 'COE','EECE','mercy.lambino@gmail.com', 'Iligan City', '09364523734', 'Professor', 'password');

INSERT INTO pc_user_meta VALUES ('2009-0207', 'Course', 'BSEC');
INSERT INTO pc_user_meta VALUES ('2009-7390', 'Course', 'BSEC');
INSERT INTO pc_user_meta VALUES ('2009-0731', 'Course', 'BSEC');
INSERT INTO pc_user_meta VALUES ('2011-1697', 'Course', 'BSCS');
INSERT INTO pc_user_meta VALUES ('2008-0886', 'Course', 'BSEC');
INSERT INTO pc_user_meta VALUES ('2009-1133', 'Course', 'BSEC');
INSERT INTO pc_user_meta VALUES ('2009-0040', 'Course', 'BSEC');
INSERT INTO pc_user_meta VALUES ('2009-1284', 'Course', 'BSEC');
INSERT INTO pc_user_meta VALUES ('2009-0567', 'Course', 'BSEC');
INSERT INTO pc_user_meta VALUES ('2009-7389', 'Course', 'BSEC');