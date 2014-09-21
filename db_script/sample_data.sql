INSERT INTO pc_account_type VALUES ('Student');
INSERT INTO pc_account_type VALUES ('Professor');

SELECT * FROM setSchedule ('07:00:00','07:30:00');
SELECT * FROM setSchedule ('07:30:00','08:00:00');
SELECT * FROM setSchedule ('08:00:00','08:30:00');
SELECT * FROM setSchedule ('08:30:00','09:00:00');

SELECT * FROM setUser ('2009-0207', row('Stephanie','Visitacion'), 'teepanot7384@gmail.com', 'Sta. Cruz, Ozamiz City', '09207278184', 'Student', 'password');
SELECT * FROM setUser ('2009-7390', row('Carmelyn','Bernal'), 'dramaPrincess1097@gmail.com', 'Brgy. Upper Hinaplanon, Iligan City', '09752150593', 'Student', 'password');
SELECT * FROM setUser ('2009-0731', row('Christopher Clint','Pacillos'), 'buhatbuhatilangtep@gmail.com', 'Tibanga, Iligan City', '09104056412', 'Student', 'password');
SELECT * FROM setUser ('2011-1697', row('Janssen James','Tesaluna'), 'janssen_snow@gmail.com', 'Brgy. Upper Hinaplanon, Iligan City', '09478392098', 'Student', 'password');
SELECT * FROM setUser ('2008-0886', row('Geomart Brenth','Abong'), 'geomart_brenth@gmail.com', 'Tibanga, Iligan City', '09355678184', 'Student', 'password');

SELECT * FROM setUser ('09-039', row('Orv1','Llan'), 'submit.proj2oel@gmail.com', 'Iligan City', '09364568754', 'Professor', 'password');
SELECT * FROM setUser ('09-039', row('Orv2','Tos'), 'submit.proj2oeT@gmail.com', 'Iligan City', '09364568754', 'Professor', 'password');

INSERT INTO pc_user_meta VALUES ('2009-0207', 'Course', 'BSEC');
INSERT INTO pc_user_meta VALUES ('2009-7390', 'Course', 'BSEC');
INSERT INTO pc_user_meta VALUES ('2009-0731', 'Course', 'BSEC');
INSERT INTO pc_user_meta VALUES ('2011-1697', 'Course', 'BSCS');
INSERT INTO pc_user_meta VALUES ('2008-0886', 'Course', 'BSEC');