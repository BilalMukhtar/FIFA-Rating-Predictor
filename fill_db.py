import psycopg2
from sqlalchemy import create_engine
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from understat_scrap_funcs import *

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

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

seasons = ["2021"]
for i in seasons:
    cur_season = get_all_teams(i, driver)
    cur_players = get_all_players(i, driver)
    cur_season.to_sql(f'teams_{i}', conn, if_exists = 'replace')
    cur_players.to_sql(f'players_{i}', conn, if_exists = 'replace')

conn1.commit()
conn1.close()


