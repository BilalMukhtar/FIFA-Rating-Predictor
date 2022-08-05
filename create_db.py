import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from understat_scrap_funcs import *
from db_tables import players, teams

driver = webdriver.Chrome("/Users/sheikhbman/Desktop/My Projects/fbdict/chromedriver")

conn_string = 'postgresql://postgres:password@localhost/db'
  
db = create_engine(conn_string)
conn = db.connect()
conn1 = psycopg2.connect(
    database="db",
  user='postgres', 
  password='password', 
  host='localhost', 
  port= '5432'
)
  
conn1.autocommit = True
cursor = conn1.cursor()

cursor.execute('drop table if exists players')
cursor.execute('drop table if exists teams')

cursor.execute(players)
cursor.execute(teams)

conn1.commit()
conn1.close()
