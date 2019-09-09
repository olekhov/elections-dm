-- Кандидаты
CREATE TABLE Candidates (
	ID integer primary key,
	candidate_name text not null,
	birthday date,
	self_nom boolean, -- самовыдвиженец
	ug boolean, -- поддержан умным голосованием
	remark text,
	FOREIGN KEY(party) REFERENCES Parties(ID)
);

-- Партии
CREATE TABLE Parties(
	ID integer primary key,
	party_name text not null,
	code text,
	remark text);

-- Связка Кандидат-Партия
CREATE TABLE C_Party_Link(
	candidate_id INTEGER,
	party_id INTEGER);

-- Связка Кандидат-ОИК
CREATE TABLE C_OIK_Link(
	candidate_id INTEGER,
	oik_id INTEGER,
	FOREIGN KEY(candidate_id) REFERENCES Candidates(ID),
	FOREIGN KEY(oik_id) REFERENCES OIK(ID)
);

