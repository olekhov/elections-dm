-- Протокол УИК
CREATE TABLE UIK_Protocol (
	ID integer primary key,
	uik_id integer,
	row_name text,
	row_number text,
	row_value integer,
	dt datetime default);


