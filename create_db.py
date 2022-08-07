import psycopg2
from sqlalchemy import create_engine
from understat_scrap_funcs import *
from db_tables import *

conn_string = 'postgresql://postgres:password@localhost/understat'
  
db = create_engine(conn_string)
conn = db.connect()
conn1 = psycopg2.connect(
    database="understat",
  user='postgres', 
  password='password', 
  host='localhost', 
  port= '5432'
)
  
conn1.autocommit = True
cursor = conn1.cursor()

seasons = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
for i in seasons:
  cursor.execute(f'drop table if exists players_{i}')
  cursor.execute(f'drop table if exists teams_{i}')
  cursor.execute(eval(f'players_{i}'))
  cursor.execute(eval(f'teams_{i}'))

conn1.commit()
conn1.close()
