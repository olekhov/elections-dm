CREATE TABLE OIKS (
	ID int primary key,
	name text not null,
	url text not null);

CREATE TABLE TIKS (
	ID int primary key,
	FOREIGN KEY(oik) REFERENCES OIKS(ID),
	name text not null,
	address TEXT,
	url TEXT NOT NULL);



