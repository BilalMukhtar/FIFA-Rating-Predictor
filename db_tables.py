teams = '''CREATE TABLE teams (
	team VARCHAR ( 50 ) PRIMARY KEY,
	league VARCHAR ( 50 ) NOT NULL,
	season FLOAT ( 10 ) NOT NULL,
	M FLOAT ( 10 ) NOT NULL,
	W FLOAT ( 10 ) NOT NULL,
    D FLOAT ( 10 ) NOT NULL,
	L FLOAT ( 10 ) NOT NULL,
	G FLOAT ( 10 ) NOT NULL,
    GA FLOAT ( 10 ) NOT NULL,
	PTS FLOAT ( 10 ) NOT NULL,
	xG FLOAT ( 10 ) NOT NULL,
    xGdiff FLOAT ( 10 ) NOT NULL,
	xGA FLOAT ( 10 ) NOT NULL,
	xGAdiff FLOAT ( 10 ) NOT NULL,
    xPTS FLOAT ( 10 ) NOT NULL,
	xPTSdiff FLOAT ( 10 ) NOT NULL,
	created_on TIMESTAMP NOT NULL,
    updated_on TIMESTAMP
    FOREIGN KEY (team)
        REFERENCES players (team),
);'''

players = '''CREATE TABLE players (
	team VARCHAR ( 50 ) PRIMARY KEY,
	league VARCHAR ( 50 ) NOT NULL,
	season FLOAT ( 10 ) NOT NULL,
	name VARCHAR ( 50 ) NOT NULL,
	pos VARCHAR ( 10 ) NOT NULL,
    apps FLOAT ( 10 ) NOT NULL,
	min FLOAT ( 10 ) NOT NULL,
	G FLOAT ( 10 ) NOT NULL,
    A FLOAT ( 10 ) NOT NULL,
	sh90 FLOAT ( 10 ) NOT NULL,
	KP90 FLOAT ( 10 ) NOT NULL,
    xG FLOAT ( 10 ) NOT NULL,
	xGdiff FLOAT ( 10 ) NOT NULL,
	xA FLOAT ( 10 ) NOT NULL,
    xAdiff FLOAT ( 10 ) NOT NULL,
	xG90 FLOAT ( 10 ) NOT NULL,
    xA90 FLOAT ( 10 ) NOT NULL,
	created_on TIMESTAMP NOT NULL,
    updated_on TIMESTAMP
    FOREIGN KEY (team)
        REFERENCES players (team),
    FOREIGN KEY (user_id)
      REFERENCES accounts (user_id)
);'''