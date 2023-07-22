DROP TABLE IF EXISTS PLAYER CASCADE;
DROP TABLE IF EXISTS CLUB CASCADE;
DROP TABLE IF EXISTS COMPETITION CASCADE;
DROP TABLE IF EXISTS PLAYER_STATS CASCADE;
DROP TABLE IF EXISTS CLUB_STATS CASCADE;
DROP TABLE IF EXISTS COMP_STATS CASCADE;
DROP TABLE IF EXISTS PLAYER_RATINGS CASCADE;

CREATE TABLE PLAYER
(
    player_id           INTEGER,
    player_id_ustat     INTEGER,
    player_name_futbin  varchar(50),
    player_name_ustat   varchar(50),
    dob                 date,
    nation              varchar(30),
    position            varchar(5),
    CONSTRAINT PK_PLAYER PRIMARY KEY (player_id)
);

CREATE TABLE CLUB
(
    club_id             INTEGER,
    club_id_futbin      INTEGER,
    club_name_futbin    varchar(100),
    club_name_ustat     varchar(100),
    nation              varchar(50),
    CONSTRAINT PK_CLUB PRIMARY KEY (club_id)
);

CREATE TABLE COMPETITION
(
    comp_id     INTEGER,
    name        varchar(50),
    region      varchar(50),
    CONSTRAINT PK_COMP PRIMARY KEY (comp_id)
);

CREATE TABLE PLAYER_STATS
(
    player_id           INTEGER,
    season              INTEGER,
    comp_id             INTEGER,
    club_id             INTEGER,
    apps                INTEGER,
    minutes             INTEGER,
    goals               INTEGER,
    "xG"                DECIMAL,
    assists             INTEGER,
    "xA"                DECIMAL,
    shots               INTEGER,
    key_passes          INTEGER,
    yellow_cards        INTEGER,
    red_cards           INTEGER,
    npg                 INTEGER,
    "npxG"              DECIMAL,
    "xGChain"           DECIMAL,
    "xGBuildup"         DECIMAL,
    CONSTRAINT PK_PLAYER_STATS PRIMARY KEY (player_id, season, comp_id, club_id),
    CONSTRAINT FK1_PLAYER_STATS FOREIGN KEY (player_id) REFERENCES PLAYER(player_id),
    CONSTRAINT FK2_PLAYER_STATS FOREIGN KEY (club_id) REFERENCES CLUB(club_id)
);

CREATE TABLE CLUB_STATS
(
    club_id             INTEGER,
    season              INTEGER,
    comp_id             INTEGER,
    wins                INTEGER,
    losses              INTEGER,
    draws               INTEGER,
    goals               INTEGER,
    assists             INTEGER,
    goals_allowed       INTEGER,
    xG                  INTEGER,
    xA                  INTEGER,
    xGA                 INTEGER,
    CONSTRAINT PK_CLUB_STATS PRIMARY KEY (club_id, season, comp_id),
    CONSTRAINT FK1_CLUB_STATS FOREIGN KEY (club_id) REFERENCES CLUB(club_id)
);

CREATE TABLE COMP_STATS
(
    comp_id             INTEGER,
    season              INTEGER,
    winner              INTEGER,
    CONSTRAINT PK_COMP_STATS PRIMARY KEY (comp_id, season)
);

CREATE TABLE PLAYER_RATINGS
(
    player_id           INTEGER,
    season              INTEGER,
    card_id             INTEGER,
    rating              INTEGER,
    pac                 INTEGER,
    acceleration        INTEGER,
    sprint_speed        INTEGER,
    dri                 INTEGER,
    agility             INTEGER,
    balance             INTEGER,
    reactions           INTEGER,
    ball_control        INTEGER,
    dribbling           INTEGER,
    composure           INTEGER,
    sho                 INTEGER,
    positioning         INTEGER,
    finishing           INTEGER,
    shot_power          INTEGER,
    long_shots          INTEGER,
    volleys             INTEGER,
    penalties           INTEGER,
    pas                 INTEGER,
    vision              INTEGER,
    crossing            INTEGER,
    fk_accuracy         INTEGER,
    short_passing       INTEGER,
    long_passing        INTEGER,
    curve               INTEGER,
    def                 INTEGER,
    interceptions       INTEGER,
    heading_acc         INTEGER,
    def_awareness       INTEGER,
    standing_tackle     INTEGER,
    sliding_tackle      INTEGER,
    phy                 INTEGER,
    jumping             INTEGER,
    stamina             INTEGER,
    strength            INTEGER,
    aggression          INTEGER,
    gk_diving           INTEGER,
    gk_handling         INTEGER,
    gk_kicking          INTEGER,
    gk_reflexes         INTEGER,
    gk_speed            INTEGER,
    gk_positioning      INTEGER,
    CONSTRAINT PK_PLAYER_RATINGS PRIMARY KEY (player_id, season),
    CONSTRAINT FK1_PLAYER_STATS FOREIGN KEY (player_id) REFERENCES PLAYER(player_id)
);