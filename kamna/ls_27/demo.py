import sqlite3 
conn = sqlite3.connect('databse.sqlite')
print ("Opened database successfully")

conn.execute('''CREATE TABLE CLASS_10
            (SNO INT PRIMARY KEY NOT NULL,)
            ROLL_NO INT NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT DEFAULT 15
            GENDER TEXT NOT NULL
            EMAIL_ID TEXT NOT NULL
             CONTACT_NO REAL NOT NULL
                );''')
print ("Table created successfully")

conn.execute("INSERT INTO CLASS_10 (SNO, ROLL_NO, NAME, AGE, GENDER, EMAIL_ID, CONTACT_NO) " \
"VALUES (1, 1, 'ALLEN', 15, 'MALE', 'allen@gmail.com', 9876543210)") 

conn.execute("INSERT INTO CLASS_10 (SNO, ROLL_NO, NAME, AGE, GENDER, EMAIL_ID, CONTACT_NO) " \
"VALUES (2, 2, 'JOHN', 15, 'MALE', 'john@gmail.com', 9876543211)")

conn.execute("INSERT INTO CLASS_10 (SNO, ROLL_NO, NAME, AGE, GENDER, EMAIL_ID, CONTACT_NO) " \
"VALUES (3, 3, 'MARY', 15, 'FEMALE', 'mary@gmail.com', 9876543212)")

conn.commit()
print ("Records created successfully")

import pandas as pd
tables = pd.read_sql_query("""SELECT *
                           FROM sqlite_master
                            WHERE type='table';""", conn)
tables

class_10d= pd.read_sql("""SELECT *
                           FROM CLASS_10;""", conn)

class_10d.head()

#Activity - 2
import pandas as pd
import numpy as np
import sqlite3

database = 'databse.sqlite'
conn = sqlite3.connect(database)
print("Opened database successfully")

df= pd.read_sql("""SELECT *
                     FROM sqlite_master
                        WHERE type='table';""", conn)
df

player_match= pd.read_sql("""SELECT *
                        FROM player_match;""", conn)
player_match.head()

null_match = pd.read_sql("""SELECT *
                                FROM player_match
                                WHERE player_id IS NULL;""", conn)
null_match

