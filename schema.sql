--  Окружные комиссии
CREATE TABLE OIKS (
	ID integer primary key,
	oik_name text not null,
	url text not null);

-- Территориальные комиссии
CREATE TABLE TIKS (
	ID integer primary key,
	oik integer,
	tik_name text not null,
	address TEXT,
	url TEXT NOT NULL,
	FOREIGN KEY(oik) REFERENCES OIKS(ID));

-- Участковые комиссии
CREATE TABLE UIKS (
	ID integer primary key,
	tik integer,
	uik_name text not null,
	address TEXT,
	url TEXT NOT NULL,
	FOREIGN KEY(tik) REFERENCES TIKS(ID));


