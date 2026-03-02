import pandas as pd
import kagglehub
import sqlite3
import os
path = kagglehub.dataset_download("notkrishna/cricket-statistics-for-all-formats")

files = os.listdir(path)
print("Files in the dataset:", files)

db_file = [f for f in os.listdir(path) if f.endswith((".sqlite", ".db"))][0]
if not db_file:
    raise FileNotFoundError("No database file found in the dataset.")
else:
   db_file = os.path.join(path, db_file)    
conn = sqlite3.connect(os.path.join(path, db_file))

match_details = pd.read_sql ("""SELECT season_id, match_id, home_team_api_id, away_team_api_id
                             , home_team_goal, away_team_goal
                                FROM Match
                            INNER JOIN VENUE ON Match.venue_id = VENUE.venue_id 
                             INNER JOIN TEAM ON Match.home_team_api_id = TEAM.team_api_id
                             INNER JOIN TEAM AS TEAM2 ON Match.away_team_api_id = TEAM2.team_api_id
                              ;""",conn)
print(match_details)
conn.close()

#Activity 2
match_details = pd.read_sql ("""SELECT season_id, match_id
                             (SELECT Venue_name
                                FROM VENUE v 
                                WHERE v.venue_id = Match.venue_id) AS Venue_name,
                                (SELECT City_name
                                FROM CITY c 
                                WHERE c.city_id = VENUE.city_id) AS City_name,
                                (SELECT team_name 
                                FROM TEAM t 
                                WHERE t.team_api_id = Match.home_team_api_id) AS winner
                                FROM Match m ;""",conn)
print(match_details)
conn.close()