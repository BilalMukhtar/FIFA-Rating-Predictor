import psycopg2
import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:password@localhost/understat'
  
db = create_engine(conn_string)
conn = db.connect()
conn1 = psycopg2.connect(
    database="understat",
  user='postgres', 
  password='password', 
  host='localhost', 
  port='5432'
)
  
conn1.autocommit = True
cursor = conn1.cursor()

seasons = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
for i in seasons:
    cur_season = pd.read_sql(f'SELECT * FROM teams_{i};', conn1)
    cur_players = pd.read_sql(f'SELECT * FROM players_{i};', conn1)
    cur_season.to_csv(f'teams_{i}.csv')
    cur_players.to_csv(f'players_{i}.csv')

conn1.commit()
conn1.close()