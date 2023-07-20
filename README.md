# FIFA Rating Predictor/DB

## Overview
In preparation for the the release of EAFC 24, I wanted to attempt to predict the ratings of some of the top players in the world. By using historical FIFA data alongside real-life stats, I attempted to accurately predict ratings of players.

## Process
* Data was scraped from futbin.com and understat.com using BeautifulSoup
* The data was then combined by matching clubs and player names manually and via fuzzy-matching
* Cleaned data was then populated into a custom made database to allow for complex queries to match-up different FIFA years with real life seasons
* DB was queried using RPostgres and then analysis was done using R

## Files
### Notebooks
* futbin_scrape/understat_scrape: used to scrape data
* data_cleaning: used to clean data and match data from both sources
* futbin_understat_combo: used to combine cleaned data into one csv file
* to_db: used to insert all cleaned data into the database

### Folders
* csv files: raw scraped data and the cleaned/combined data
* data repair csvs: csvs used to match player names and clubs
* sql files: file to create database with correct constraints

## Database
Based on the following diagram, the goal is to expand the project to also contain data from teams which may improve the current predictions along with allowing for future projects/analysis
[![Watch the video][(https://i.stack.imgur.com/Vp2cE.png](https://github.com/BilalMukhtar/FIFA-Rating-Predictor/blob/main/imgs/soccer_db_png.png))]([https://youtu.be/vt5fpE0bzSY](https://drawsql.app/teams/bilals-team-1/diagrams/soccerdb/embed))


## Data Sources
* futbin.com (FIFA Data)
* understat.com (Player Data)
