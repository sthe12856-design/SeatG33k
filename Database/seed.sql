PRAGMA foreign_keys = ON;

BEGIN TRANSACTION;

-- ─────────────────────────────────────────────
--  MANAGERS  (one per division)
-- ─────────────────────────────────────────────
INSERT INTO manager (manager_id, first_name, last_name, contact_no, email_address, password_hash) VALUES
(1, 'Andile', 'Mahlaba', '0711000001', 'andile.manager@seatg33k.com', 'placeholder_hash');

-- ─────────────────────────────────────────────
--  DIVISIONS
--  Div A → manager 1 | 24 participants | 8/session
--  Div B → manager 2 | 18 participants | 6/session
--  Div C → manager 3 | 18 participants | 6/session
-- ─────────────────────────────────────────────
INSERT INTO division (div_id, manager_id, name) VALUES
(1, 1, 'Division A'),
(2, 1, 'Division B'),
(3, 1, 'Division C');

-- ─────────────────────────────────────────────
--  PARTICIPANTS  (60 total)
--  IDs  1-24  → Division A
--  IDs 25-42  → Division B
--  IDs 43-60  → Division C
-- ─────────────────────────────────────────────
INSERT INTO participant (participant_id, first_name, last_name, contact_no, email_address, password_hash) VALUES
-- Division A (24)
( 1, 'Sipho',        'Dlamini',     '0821000001', 'sipho.dlamini@seatg33k.com',       'placeholder_hash'),
( 2, 'Nomsa',        'Nkosi',       '0821000002', 'nomsa.nkosi@seatg33k.com',         'placeholder_hash'),
( 3, 'Bongani',      'Zulu',        '0821000003', 'bongani.zulu@seatg33k.com',        'placeholder_hash'),
( 4, 'Thandi',       'Mthembu',     '0821000004', 'thandi.mthembu@seatg33k.com',      'placeholder_hash'),
( 5, 'Lungelo',      'Ndlovu',      '0821000005', 'lungelo.ndlovu@seatg33k.com',      'placeholder_hash'),
( 6, 'Zanele',       'Khumalo',     '0821000006', 'zanele.khumalo@seatg33k.com',      'placeholder_hash'),
( 7, 'Nhlanhla',     'Ntuli',       '0821000007', 'nhlanhla.ntuli@seatg33k.com',      'placeholder_hash'),
( 8, 'Lindiwe',      'Cele',        '0821000008', 'lindiwe.cele@seatg33k.com',        'placeholder_hash'),
( 9, 'Sandile',      'Mhlongo',     '0821000009', 'sandile.mhlongo@seatg33k.com',     'placeholder_hash'),
(10, 'Ayanda',       'Shabalala',   '0821000010', 'ayanda.shabalala@seatg33k.com',    'placeholder_hash'),
(11, 'Mbuso',        'Ngcobo',      '0821000011', 'mbuso.ngcobo@seatg33k.com',        'placeholder_hash'),
(12, 'Nokukhanya',   'Majola',      '0821000012', 'nokukhanya.majola@seatg33k.com',   'placeholder_hash'),
(13, 'Thulani',      'Mkhize',      '0821000013', 'thulani.mkhize@seatg33k.com',      'placeholder_hash'),
(14, 'Nomvula',      'Mnguni',      '0821000014', 'nomvula.mnguni@seatg33k.com',      'placeholder_hash'),
(15, 'Sifiso',       'Buthelezi',   '0821000015', 'sifiso.buthelezi@seatg33k.com',    'placeholder_hash'),
(16, 'Nokwanda',     'Zondo',       '0821000016', 'nokwanda.zondo@seatg33k.com',      'placeholder_hash'),
(17, 'Mthokozisi',   'Mthethwa',    '0821000017', 'mthokozisi.mthethwa@seatg33k.com', 'placeholder_hash'),
(18, 'Phumzile',     'Gumede',      '0821000018', 'phumzile.gumede@seatg33k.com',     'placeholder_hash'),
(19, 'Khulekani',    'Vilakazi',    '0821000019', 'khulekani.vilakazi@seatg33k.com',  'placeholder_hash'),
(20, 'Bongiwe',      'Sithole',     '0821000020', 'bongiwe.sithole@seatg33k.com',     'placeholder_hash'),
(21, 'Mpendulo',     'Dube',        '0821000021', 'mpendulo.dube@seatg33k.com',       'placeholder_hash'),
(22, 'Nokwazi',      'Nxumalo',     '0821000022', 'nokwazi.nxumalo@seatg33k.com',     'placeholder_hash'),
(23, 'Sibonelo',     'Molefe',      '0821000023', 'sibonelo.molefe@seatg33k.com',     'placeholder_hash'),
(24, 'Ntombifikile', 'Radebe',      '0821000024', 'ntombifikile.radebe@seatg33k.com', 'placeholder_hash'),
-- Division B (18)
(25, 'Lerato',       'Mokoena',     '0821000025', 'lerato.mokoena@seatg33k.com',      'placeholder_hash'),
(26, 'Thabo',        'Phiri',       '0821000026', 'thabo.phiri@seatg33k.com',         'placeholder_hash'),
(27, 'Palesa',       'Modise',      '0821000027', 'palesa.modise@seatg33k.com',       'placeholder_hash'),
(28, 'Katlego',      'Mahlangu',    '0821000028', 'katlego.mahlangu@seatg33k.com',    'placeholder_hash'),
(29, 'Refilwe',      'Nkosi',       '0821000029', 'refilwe.nkosi@seatg33k.com',       'placeholder_hash'),
(30, 'Tumelo',       'Matlala',     '0821000030', 'tumelo.matlala@seatg33k.com',      'placeholder_hash'),
(31, 'Boitumelo',    'Kgomo',       '0821000031', 'boitumelo.kgomo@seatg33k.com',     'placeholder_hash'),
(32, 'Dineo',        'Sello',       '0821000032', 'dineo.sello@seatg33k.com',         'placeholder_hash'),
(33, 'Keabetswe',    'Moshoeshoe',  '0821000033', 'keabetswe.moshoeshoe@seatg33k.com','placeholder_hash'),
(34, 'Motlatsi',     'Tau',         '0821000034', 'motlatsi.tau@seatg33k.com',        'placeholder_hash'),
(35, 'Malerato',     'Molefe',      '0821000035', 'malerato.molefe@seatg33k.com',     'placeholder_hash'),
(36, 'Nthabi',       'Dlamini',     '0821000036', 'nthabi.dlamini@seatg33k.com',      'placeholder_hash'),
(37, 'Tebogo',       'Sefako',      '0821000037', 'tebogo.sefako@seatg33k.com',       'placeholder_hash'),
(38, 'Kagiso',       'Mosia',       '0821000038', 'kagiso.mosia@seatg33k.com',        'placeholder_hash'),
(39, 'Nthabiseng',   'Ramphele',    '0821000039', 'nthabiseng.ramphele@seatg33k.com', 'placeholder_hash'),
(40, 'Lebogang',     'Mogale',      '0821000040', 'lebogang.mogale@seatg33k.com',     'placeholder_hash'),
(41, 'Goitseone',    'Masilo',      '0821000041', 'goitseone.masilo@seatg33k.com',    'placeholder_hash'),
(42, 'Tshepiso',     'Seleke',      '0821000042', 'tshepiso.seleke@seatg33k.com',     'placeholder_hash'),
-- Division C (18)
(43, 'Anele',        'Mthembu',     '0821000043', 'anele.mthembu@seatg33k.com',       'placeholder_hash'),
(44, 'Zandile',      'Mbatha',      '0821000044', 'zandile.mbatha@seatg33k.com',      'placeholder_hash'),
(45, 'Lwando',       'Majola',      '0821000045', 'lwando.majola@seatg33k.com',       'placeholder_hash'),
(46, 'Noxolo',       'Ntuli',       '0821000046', 'noxolo.ntuli@seatg33k.com',        'placeholder_hash'),
(47, 'Siyanda',      'Cele',        '0821000047', 'siyanda.cele@seatg33k.com',        'placeholder_hash'),
(48, 'Khanya',       'Shabalala',   '0821000048', 'khanya.shabalala@seatg33k.com',    'placeholder_hash'),
(49, 'Nolwazi',      'Mhlongo',     '0821000049', 'nolwazi.mhlongo@seatg33k.com',     'placeholder_hash'),
(50, 'Mondli',       'Ngcobo',      '0821000050', 'mondli.ngcobo@seatg33k.com',       'placeholder_hash'),
(51, 'Thandeka',     'Gumede',      '0821000051', 'thandeka.gumede@seatg33k.com',     'placeholder_hash'),
(52, 'Lungisa',      'Buthelezi',   '0821000052', 'lungisa.buthelezi@seatg33k.com',   'placeholder_hash'),
(53, 'Nokubonga',    'Zondo',       '0821000053', 'nokubonga.zondo@seatg33k.com',     'placeholder_hash'),
(54, 'Sibusiso',     'Mkhize',      '0821000054', 'sibusiso.mkhize@seatg33k.com',     'placeholder_hash'),
(55, 'Lethiwe',      'Vilakazi',    '0821000055', 'lethiwe.vilakazi@seatg33k.com',    'placeholder_hash'),
(56, 'Mthunzi',      'Dube',        '0821000056', 'mthunzi.dube@seatg33k.com',        'placeholder_hash'),
(57, 'Nobuhle',      'Nxumalo',     '0821000057', 'nobuhle.nxumalo@seatg33k.com',     'placeholder_hash'),
(58, 'Lungelo',      'Sithole',     '0821000058', 'lungelo.sithole@seatg33k.com',     'placeholder_hash'),
(59, 'Ntombizodwa',  'Radebe',      '0821000059', 'ntombizodwa.radebe@seatg33k.com',  'placeholder_hash'),
(60, 'Wiseman',      'Mokoena',     '0821000060', 'wiseman.mokoena@seatg33k.com',     'placeholder_hash');

-- ─────────────────────────────────────────────
--  DIVISION ↔ PARTICIPANT  memberships
-- ─────────────────────────────────────────────
INSERT INTO division_participant (div_id, participant_id) VALUES
-- Division A
(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),
(1,9),(1,10),(1,11),(1,12),(1,13),(1,14),(1,15),(1,16),
(1,17),(1,18),(1,19),(1,20),(1,21),(1,22),(1,23),(1,24),
-- Division B
(2,25),(2,26),(2,27),(2,28),(2,29),(2,30),
(2,31),(2,32),(2,33),(2,34),(2,35),(2,36),
(2,37),(2,38),(2,39),(2,40),(2,41),(2,42),
-- Division C
(3,43),(3,44),(3,45),(3,46),(3,47),(3,48),
(3,49),(3,50),(3,51),(3,52),(3,53),(3,54),
(3,55),(3,56),(3,57),(3,58),(3,59),(3,60);

-- ─────────────────────────────────────────────
--  SESSIONS  (3 shared organisation-wide sessions)
--  Total capacity 20 per session = 8 (DivA) + 6 (DivB) + 6 (DivC)
-- ─────────────────────────────────────────────
INSERT INTO session (sess_id, name, max_participants, starts_at, ends_at, status) VALUES
(1, 'Morning Session',   20, '09:00', '10:30', 'open'),
(2, 'Midday Session',    20, '11:00', '12:30', 'open'),
(3, 'Afternoon Session', 20, '13:00', '14:30', 'open');

-- ─────────────────────────────────────────────
--  DIVISION QUOTAS PER SESSION
--  Division A → 8/session | Division B → 6/session | Division C → 6/session
-- ─────────────────────────────────────────────
INSERT INTO session_division_limit (sess_id, div_id, max_seats) VALUES
(1,1,8),(1,2,6),(1,3,6),
(2,1,8),(2,2,6),(2,3,6),
(3,1,8),(3,2,6),(3,3,6);

-- ─────────────────────────────────────────────
--  SEATS  (20 per session × 3 sessions = 60 total)
--  Seat IDs  1-20 → Morning   (sess 1)
--  Seat IDs 21-40 → Midday    (sess 2)
--  Seat IDs 41-60 → Afternoon (sess 3)
-- ─────────────────────────────────────────────
INSERT INTO seat (seat_id, sess_id, seat_label, is_accessible, is_active) VALUES
-- Session 1 – Morning (20 seats)
( 1,1,'01',0,1),( 2,1,'02',0,1),( 3,1,'03',0,1),( 4,1,'04',0,1),( 5,1,'05',0,1),
( 6,1,'06',0,1),( 7,1,'07',0,1),( 8,1,'08',0,1),( 9,1,'09',0,1),(10,1,'10',0,1),
(11,1,'11',0,1),(12,1,'12',0,1),(13,1,'13',0,1),(14,1,'14',0,1),(15,1,'15',1,1),
(16,1,'16',1,1),(17,1,'17',1,1),(18,1,'18',1,1),(19,1,'19',1,1),(20,1,'20',1,1),
-- Session 2 – Midday (20 seats)
(21,2,'01',0,1),(22,2,'02',0,1),(23,2,'03',0,1),(24,2,'04',0,1),(25,2,'05',0,1),
(26,2,'06',0,1),(27,2,'07',0,1),(28,2,'08',0,1),(29,2,'09',0,1),(30,2,'10',0,1),
(31,2,'11',0,1),(32,2,'12',0,1),(33,2,'13',0,1),(34,2,'14',0,1),(35,2,'15',1,1),
(36,2,'16',1,1),(37,2,'17',1,1),(38,2,'18',1,1),(39,2,'19',1,1),(40,2,'20',1,1),
-- Session 3 – Afternoon (20 seats)
(41,3,'01',0,1),(42,3,'02',0,1),(43,3,'03',0,1),(44,3,'04',0,1),(45,3,'05',0,1),
(46,3,'06',0,1),(47,3,'07',0,1),(48,3,'08',0,1),(49,3,'09',0,1),(50,3,'10',0,1),
(51,3,'11',0,1),(52,3,'12',0,1),(53,3,'13',0,1),(54,3,'14',0,1),(55,3,'15',1,1),
(56,3,'16',1,1),(57,3,'17',1,1),(58,3,'18',1,1),(59,3,'19',1,1),(60,3,'20',1,1);

-- ─────────────────────────────────────────────
--  ENROLLMENTS  (60 participants, one session each)
--
--  Morning   (sess 1):
--    DivA p1-p8   → seats 1-8
--    DivB p25-p30 → seats 9-14
--    DivC p43-p48 → seats 15-20
--
--  Midday    (sess 2):
--    DivA p9-p16  → seats 21-28
--    DivB p31-p36 → seats 29-34
--    DivC p49-p54 → seats 35-40
--
--  Afternoon (sess 3):
--    DivA p17-p24 → seats 41-48
--    DivB p37-p42 → seats 49-54
--    DivC p55-p60 → seats 55-60
-- ─────────────────────────────────────────────
INSERT INTO session_enrollment (sess_id, participant_id, seat_id) VALUES
-- Morning – Div A (p1-p8, seats 1-8)
(1, 1, 1),(1, 2, 2),(1, 3, 3),(1, 4, 4),(1, 5, 5),(1, 6, 6),(1, 7, 7),(1, 8, 8),
-- Morning – Div B (p25-p30, seats 9-14)
(1,25, 9),(1,26,10),(1,27,11),(1,28,12),(1,29,13),(1,30,14),
-- Morning – Div C (p43-p48, seats 15-20)
(1,43,15),(1,44,16),(1,45,17),(1,46,18),(1,47,19),(1,48,20),
-- Midday – Div A (p9-p16, seats 21-28)
(2, 9,21),(2,10,22),(2,11,23),(2,12,24),(2,13,25),(2,14,26),(2,15,27),(2,16,28),
-- Midday – Div B (p31-p36, seats 29-34)
(2,31,29),(2,32,30),(2,33,31),(2,34,32),(2,35,33),(2,36,34),
-- Midday – Div C (p49-p54, seats 35-40)
(2,49,35),(2,50,36),(2,51,37),(2,52,38),(2,53,39),(2,54,40),
-- Afternoon – Div A (p17-p24, seats 41-48)
(3,17,41),(3,18,42),(3,19,43),(3,20,44),(3,21,45),(3,22,46),(3,23,47),(3,24,48),
-- Afternoon – Div B (p37-p42, seats 49-54)
(3,37,49),(3,38,50),(3,39,51),(3,40,52),(3,41,53),(3,42,54),
-- Afternoon – Div C (p55-p60, seats 55-60)
(3,55,55),(3,56,56),(3,57,57),(3,58,58),(3,59,59),(3,60,60);

COMMIT;
