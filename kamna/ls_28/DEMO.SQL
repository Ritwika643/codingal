INSERT INTO Player VALUES

(1, 'Rohit', 'Batsman'),

(2, 'Virat', 'Batsman'),

(3, 'Hardik', 'All-Rounder'),

(4, 'Bumrah', 'Bowler'),

(5, 'Gill', 'Batsman'); -- This player will not play any match

INSERT INTO Match VALUES

(101, '2026-01-10', 'Warriors'),

(102, '2026-01-15', 'Titans'),

(103, '2026-01-20', 'Royals'); -- This match will have no player data

INSERT INTO Player_Match VALUES

(1, 101, 75, 0),

(2, 101, 60, 0),

(3, 101, 40, 2),

(4, 101, 10, 3),

(1, 102, 55, 0),

(2, 102, 88, 0),

(3, 102, 35, 1),

(4, 102, 5, 4);
CREATE TABLE Player (

player_id INTEGER PRIMARY KEY,

player_name TEXT,

role TEXT

);

CREATE TABLE Match (

match_id INTEGER PRIMARY KEY,

match_date DATE,

opponent TEXT

);

CREATE TABLE Player_Match (

player_id INTEGER,

match_id INTEGER,

runs_scored INTEGER,

wickets_taken INTEGER,

FOREIGN KEY (player_id) REFERENCES Player(player_id),

FOREIGN KEY (match_id) REFERENCES Match(match_id)
);

SELECT p.player_name, m.opponent, pm.runs_scored, pm.wickets_taken
FROM Player p
INNER JOIN Player_Match pm ON p.player_id = pm.player_id
INNER JOIN Match m ON pm.match_id = m.match_id;

SELECT p.player_name, m.opponent, pm.runs_scored, pm.wickets_taken
FROM Player p
LEFT JOIN Player_Match pm ON p.player_id = pm.player_id
ON pm.match_id = m.match_id;

SELECT p.player_name, m.opponent, pm.runs_scored, pm.wickets_taken
FROM Player p
RIGHT JOIN Player_Match pm ON p.player_id = pm.player_id
ON pm.match_id = m.match_id;
