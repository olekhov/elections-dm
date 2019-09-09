-- Протокол УИК
CREATE TABLE UIK_Protocol (
	ID integer primary key,
	uik_id integer,
	row_number text,
	row_name text,
	row_value integer,
	row_order integer,
	dt datetime default);


