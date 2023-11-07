CREATE DATABASE IF NOT EXISTS cpsc408;
USE cpsc408;


CREATE TABLE PremTable(
	FinalRank INTEGER,
    Squad VARCHAR(50),
    MatchesPlayed INTEGER,
    Wins INTEGER,
    Draws INTEGER,
    Losses INTEGER,
    GoalsFor INTEGER,
    GoalsAllowed INTEGER,
    GoalDifferential INTEGER,
    Points INTEGER,
    ExpectedGoals float,
    ExpectedGoalsAllowed float,
    ExpectedGoalDifferential float,
    ExpGoalDiffPer90 float,
    Attendance INTEGER,
    TopTeamScorer varchar(50), 
    Goalkeeper varchar(50),
    Notes varchar(100)
);

CREATE TABLE SeriaATable(
	FinalRank INTEGER,
    Squad VARCHAR(50),
    MatchesPlayed INTEGER,
    Wins INTEGER,
    Draws INTEGER,
    Losses INTEGER,
    GoalsFor INTEGER,
    GoalsAllowed INTEGER,
    GoalDifferential INTEGER,
    Points INTEGER,
    ExpectedGoals float,
    ExpectedGoalsAllowed float,
    ExpectedGoalDifferential float,
    ExpGoalDiffPer90 float,
    Attendance INTEGER,
    TopTeamScorer varchar(50), 
    Goalkeeper varchar(50),
    Notes varchar(100)
);




CREATE TABLE Ligue1Table(
	FinalRank INTEGER, 
    Squad VARCHAR(50),
    MatchesPlayed INTEGER,
    Wins INTEGER,
    Draws INTEGER,
    Losses INTEGER,
    GoalsFor INTEGER,
    GoalsAllowed INTEGER,
    GoalDifferential INTEGER,
    Points INTEGER,
    ExpectedGoals float,
    ExpectedGoalsAllowed float,
    ExpectedGoalDifferential float, 
    ExpGoalDiffPer90 float,
    Last5Results varchar(25),
    Attendance INTEGER,
    TopTeamScorer varchar(50),
    Goalkeeper varchar(50)
);

CREATE TABLE LaLigaTable(
	FinalRank INTEGER,
    Squad VARCHAR(50),
    MatchesPlayed INTEGER,
    Wins INTEGER,
    Draws INTEGER,
    Losses INTEGER,
    GoalsFor INTEGER,
    GoalsAllowed INTEGER,
    GoalDifferential INTEGER,
    Points INTEGER,
    ExpectedGoals float,
    ExpectedGoalsAllowed float,
    ExpectedGoalDifferential float,
    ExpGoalDiffPer90 float,
    Attendance INTEGER,
    TopTeamScorer varchar(50), 
    Goalkeeper varchar(50),
    Notes varchar(100)
);

CREATE TABLE BundesligaTable(
	FinalRank INTEGER,
    Squad VARCHAR(50),
    MatchesPlayed INTEGER,
    Wins INTEGER,
    Draws INTEGER,
    Losses INTEGER,
    GoalsFor INTEGER,
    GoalsAllowed INTEGER,
    GoalDifferential INTEGER,
    Points INTEGER,
    ExpectedGoals float,
    ExpectedGoalsAllowed float,
    ExpectedGoalDifferential float,
    ExpGoalDiffPer90 float,
    Attendance INTEGER,
    TopTeamScorer varchar(50), 
    Goalkeeper varchar(50),
    Notes varchar(100)
);

-- DROP TABLE SerieAPlayers; 

CREATE TABLE SerieAPlayers(
Rk  INTEGER PRIMARY KEY auto_increment,
Player VARCHAR(50),
Nation VARCHAR(50),
Position VARCHAR(50),
Squad VARCHAR(50),
Age INTEGER,
Born YEAR,
NinetyMinsPlayed float,
YellowCards INTEGER,
RedCards INTEGER,
SecondYellow INTEGER,
FoulsCommitted INTEGER,
FoulsDrawn INTEGER,
Offsides INTEGER,
Crosses INTEGER,
Interceptions INTEGER,
TacklesWon INTEGER,
PKwon INTEGER,
PKConceded INTEGER,
OwnGoals INTEGER,
BallsRecovered INTEGER,
AerialsWon INTEGER,
AerialsLost INTEGER,
WonPercentage float
);

-- DROP TABLE PremPlayers;

CREATE TABLE PremPlayers(
Rk  INTEGER PRIMARY KEY auto_increment,
Player VARCHAR(50),
Nation VARCHAR(50),
Position VARCHAR(50),
Squad VARCHAR(50),
Age INTEGER,
Born YEAR,
NinetyMinsPlayed float,
YellowCards INTEGER,
RedCards INTEGER,
SecondYellow INTEGER,
FoulsCommitted INTEGER,
FoulsDrawn INTEGER,
Offsides INTEGER,
Crosses INTEGER,
Interceptions INTEGER,
TacklesWon INTEGER,
PKwon INTEGER,
PKConceded INTEGER,
OwnGoals INTEGER,
BallsRecovered INTEGER,
AerialsWon INTEGER,
AerialsLost INTEGER,
WonPercentage float
);

-- DROP TABLE LaLigaPlayers;
CREATE TABLE LaLigaPlayers(
Rk  INTEGER PRIMARY KEY auto_increment,
Player VARCHAR(50),
Nation VARCHAR(50),
Position VARCHAR(50),
Squad VARCHAR(50),
Age INTEGER,
Born YEAR,
NinetyMinsPlayed float,
YellowCards INTEGER,
RedCards INTEGER,
SecondYellow INTEGER,
FoulsCommitted INTEGER,
FoulsDrawn INTEGER,
Offsides INTEGER,
Crosses INTEGER,
Interceptions INTEGER,
TacklesWon INTEGER,
PKwon INTEGER,
PKConceded INTEGER,
OwnGoals INTEGER,
BallsRecovered INTEGER,
AerialsWon INTEGER,
AerialsLost INTEGER,
WonPercentage float
);

-- DROP TABLE Ligue1Players;
CREATE TABLE Ligue1Players(
Rk  INTEGER PRIMARY KEY auto_increment,
Player VARCHAR(50),
Nation VARCHAR(50),
Position VARCHAR(50),
Squad VARCHAR(50),
AgeYears_Days VARCHAR(10),
Born YEAR,
NinetyMinsPlayed float,
YellowCards INTEGER,
RedCards INTEGER,
SecondYellow INTEGER,
FoulsCommitted INTEGER,
FoulsDrawn INTEGER,
Offsides INTEGER,
Crosses INTEGER,
Interceptions INTEGER,
TacklesWon INTEGER,
PKwon INTEGER,
PKConceded INTEGER,
OwnGoals INTEGER,
BallsRecovered INTEGER,
AerialsWon INTEGER,
AerialsLost INTEGER,
WonPercentage float
);

-- DROP TABLE BundesligaPlayers;

CREATE TABLE BundesligaPlayers(
Rk  INTEGER PRIMARY KEY auto_increment,
Player VARCHAR(50),
Nation VARCHAR(50),
Position VARCHAR(50),
Squad VARCHAR(50),
Age INTEGER,
Born YEAR,
NinetyMinsPlayed float,
YellowCards INTEGER,
RedCards INTEGER,
SecondYellow INTEGER,
FoulsCommitted INTEGER,
FoulsDrawn INTEGER,
Offsides INTEGER,
Crosses INTEGER,
Interceptions INTEGER,
TacklesWon INTEGER,
PKwon INTEGER,
PKConceded INTEGER,
OwnGoals INTEGER,
BallsRecovered INTEGER,
AerialsWon INTEGER,
AerialsLost INTEGER,
WonPercentage float
);



CREATE TABLE PREMFIXTURES(
MatchWeek INTEGER,
DayofWeek VARCHAR(3),
Date DATE,
LocalTimeofGame varchar(20),
HomeTeam VARCHAR(30),
ExpectedHomeGoals FLOAT,
HomeGoals INTEGER,
Score VARCHAR(10),
AwayGoals INTEGER,
ExpectedAwayGoals FLOAT,
AwayTeam VARCHAR(30),
Attendance INTEGER,
Venue VARCHAR(100),
Referee VARCHAR(30)
);


CREATE TABLE LALIGAFIXTURES(
MatchWeek INTEGER,
DayofWeek VARCHAR(3),
Date DATE,
LocalTimeofGame varchar(20),
HomeTeam VARCHAR(30),
ExpectedHomeGoals FLOAT,
HomeGoals INTEGER,
Score VARCHAR(10),
AwayGoals INTEGER,
ExpectedAwayGoals FLOAT,
AwayTeam VARCHAR(30),
Attendance INTEGER,
Venue VARCHAR(100),
Referee VARCHAR(30)
);

-- DROP TABLE LIGUE1FIXTURES; 

CREATE TABLE LIGUE1FIXTURES(
MatchWeek INTEGER,
DayofWeek VARCHAR(3),
Date DATE,
LocalTimeofGame varchar(20),
HomeTeam VARCHAR(30),
ExpectedHomeGoals FLOAT,
Score VARCHAR(10),
ExpectedAwayGoals FLOAT,
AwayTeam VARCHAR(30),
Attendance INTEGER,
Venue VARCHAR(100),
Referee VARCHAR(30)
);



-- SELECT * FROM SERIEAFIXTURES; 
CREATE TABLE SERIEAFIXTURES(
MatchWeek INTEGER,
DayofWeek VARCHAR(3),
Date DATE,
LocalTimeofGame varchar(20),
HomeTeam VARCHAR(30),
ExpectedHomeGoals FLOAT,
HomeGoals INTEGER,
Score VARCHAR(10),
AwayGoals INTEGER,
ExpectedAwayGoals FLOAT,
AwayTeam VARCHAR(30),
Attendance INTEGER,
Venue VARCHAR(100),
Referee VARCHAR(30)
);

-- SELECT * FROM BUNDESLIGAFIXTURES;

CREATE TABLE BUNDESLIGAFIXTURES(
MatchWeek INTEGER,
DayofWeek VARCHAR(3),
Date DATE,
LocalTimeofGame varchar(20),
HomeTeam VARCHAR(30),
ExpectedHomeGoals FLOAT,
HomeGoals INTEGER,
Score VARCHAR(10),
AwayGoals INTEGER,
ExpectedAwayGoals FLOAT,
AwayTeam VARCHAR(30),
Attendance INTEGER,
Venue VARCHAR(100),
Referee VARCHAR(30)
);




-- -- DROP TABLE PREMFIXTURES;
CREATE TABLE PREMFIXTURES(
MatchWeek INTEGER,
DayofWeek VARCHAR(3),
Date DATE,
LocalTimeofGame varchar(20),
HomeTeam VARCHAR(30),
ExpectedHomeGoals FLOAT,
Score VARCHAR(10),
ExpectedAwayGoals FLOAT,
AwayTeam VARCHAR(30),
Attendance INTEGER,
Venue VARCHAR(100),
Referee VARCHAR(30)
);



CREATE TABLE LALIGAFIXTURES(
MatchWeek INTEGER,
DayofWeek VARCHAR(3),
Date DATE,
LocalTimeofGame varchar(20),
HomeTeam VARCHAR(30),
ExpectedHomeGoals FLOAT,
Score VARCHAR(10),
ExpectedAwayGoals FLOAT,
AwayTeam VARCHAR(30),
Attendance INTEGER,
Venue VARCHAR(100),
Referee VARCHAR(30)
);

-- drop table LIGUE1FIXTURES;
-- SELECT * FROM LIGUE1FIXTURES;
CREATE TABLE LIGUE1FIXTURES(
MatchWeek INTEGER,
DayofWeek VARCHAR(3),
Date DATE,
LocalTimeofGame varchar(20),
HomeTeam VARCHAR(30),
ExpectedHomeGoals FLOAT,
Score VARCHAR(10),
ExpectedAwayGoals FLOAT,
AwayTeam VARCHAR(30),
Attendance INTEGER,
Venue VARCHAR(100),
Referee VARCHAR(30)
);

-- drop table SERIEAFIXTURES; 
-- SELECT * FROM SERIEAFIXTURES;
CREATE TABLE SERIEAFIXTURES(
MatchWeek INTEGER,
DayofWeek VARCHAR(3),
Date DATE,
LocalTimeofGame varchar(20),
HomeTeam VARCHAR(30),
ExpectedHomeGoals FLOAT,
Score VARCHAR(10),
ExpectedAwayGoals FLOAT,
AwayTeam VARCHAR(30),
Attendance INTEGER,
Venue VARCHAR(100),
Referee VARCHAR(30)
);

-- drop table BUNDESLIGAFIXTURES;

CREATE TABLE BUNDESLIGAFIXTURES(
MatchWeek INTEGER,
DayofWeek VARCHAR(3),
Date DATE,
LocalTimeofGame varchar(20),
HomeTeam VARCHAR(30),
ExpectedHomeGoals FLOAT,
Score VARCHAR(10),
ExpectedAwayGoals FLOAT,
AwayTeam VARCHAR(30),
Attendance INTEGER,
Venue VARCHAR(100),
Referee VARCHAR(30)
);


CREATE TABLE Leagues(
leagueID INTEGER PRIMARY KEY auto_increment,
leagueName VARCHAR(30),
Country VARCHAR(30)

);

INSERT INTO Leagues (leagueName,Country)
VALUES ("Bundesliga","Germany"),
("LaLiga","Spain"),
("Ligue1","Spain"),
("PremierLeague","England"),
("SeriaA","Italy")
;

