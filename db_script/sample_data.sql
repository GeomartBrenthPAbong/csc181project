INSERT INTO pc_account_type VALUES ('Student');
INSERT INTO pc_account_type VALUES ('Professor');

SELECT * FROM setSchedule ('07:00:00','07:30:00');
SELECT * FROM setSchedule ('07:30:00','08:00:00');
SELECT * FROM setSchedule ('08:00:00','08:30:00');
SELECT * FROM setSchedule ('08:30:00','09:00:00');

SELECT * FROM setUser ('2009-0207', row('Stephanie','Visitacion'), 'COE','EECE''teepanot7384@gmail.com', 'Sta. Cruz, Ozamiz City', '09207278184', 'Student', 'password');
SELECT * FROM setUser ('2009-7390', row('Carmelyn','Bernal'), 'COE','EECE','dramaPrincess1097@gmail.com', 'Brgy. Upper Hinaplanon, Iligan City', '09752150593', 'Student', 'password');
SELECT * FROM setUser ('2009-0731', row('Christopher Clint','Pacillos'), 'COE','EECE','buhatbuhatilangtep@gmail.com', 'Tibanga, Iligan City', '09104056412', 'Student', 'password');
SELECT * FROM setUser ('2011-1697', row('Janssen James','Tesaluna'), 'SCS','CS','janssen_snow@gmail.com', 'Brgy. Upper Hinaplanon, Iligan City', '09478392098', 'Student', 'password');
SELECT * FROM setUser ('2008-0886', row('Geomart Brenth','Abong'), 'COE','EECE','geomart_brenth@gmail.com', 'Tibanga, Iligan City', '09355678184', 'Student', 'password');

SELECT * FROM setUser ('09-039', row('Orv1','Llan'), 'SCS','CS','submit.proj2oel@gmail.com', 'Iligan City', '09364568754', 'Professor', 'password');
SELECT * FROM setUser ('09-038', row('Orv2','Tos'), 'SCS','CS','submit.proj2oeT@gmail.com', 'Iligan City', '09364568754', 'Professor', 'password');

INSERT INTO pc_user_meta VALUES ('2009-0207', 'Course', 'BSEC');
INSERT INTO pc_user_meta VALUES ('2009-7390', 'Course', 'BSEC');
INSERT INTO pc_user_meta VALUES ('2009-0731', 'Course', 'BSEC');
INSERT INTO pc_user_meta VALUES ('2011-1697', 'Course', 'BSCS');
INSERT INTO pc_user_meta VALUES ('2008-0886', 'Course', 'BSEC');