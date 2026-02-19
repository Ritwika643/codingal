import sqlite3
database = 'database.sqlite'
conn = sqlite3.connect(database)
print('Connected to database successfully')
matches = pd.read_sql('SELECT * FROM Match', conn)
matches.head()

result1 = pd.read_sql("""SELECT Avg(Win_Margin), Match_Winner
                    FROM Match
                    WHERE SEASON_ID == 2015
                    GROUP BY Match_Winner
                    ORDER BY Avg(Win_Margin) DESC
                        """, conn)

result1
result2 = pd.read_sql("""SELECT COUNT, ( DISTINCT VENUE_ID)
                      FROM Match
                        WHERE SEASON_ID == 2015
                      ;""", conn)
result2

Also get the total number of players who have received the man of the match throughout all seasons.
result3 = pd.read_sql("""SELECT MIN(Win_Margin), MAX(Win_Margin), AVG(Win_Margin), COUNT(DISTINCT(MAN_OF_MATCH_ID))
                    FROM Match
                      """, conn)

result3

result4 = pd.read_sql("""SELECT SUM(Win_Margin)
                      FROM Match
                        WHERE SEASON_ID == 2015
                        ;""", conn)
result4
