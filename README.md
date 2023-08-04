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
* [`futbin_scrape.ipynb`](https://github.com/BilalMukhtar/FIFA-Rating-Predictor/blob/main/futbin_scrape.ipynb) ([nbviewer version](https://nbviewer.org/github/BilalMukhtar/FIFA-Rating-Predictor/blob/main/futbin_scrape.ipynb)): scrape FIFA/EAFC data from [futbin.com](futbin.com)
* [`understat_scrape.ipynb`](https://github.com/BilalMukhtar/FIFA-Rating-Predictor/blob/main/understat_scrape.ipynb) ([nbviewer version](https://nbviewer.org/github/BilalMukhtar/FIFA-Rating-Predictor/blob/main/understat_scrape.ipynb)): scrape player stats from [understat.com](understat.com)
* [`futbin_understat_combo.ipynb`](https://github.com/BilalMukhtar/FIFA-Rating-Predictor/blob/main/futbin_understat_combo.ipynb) ([nbviewer version](https://nbviewer.org/github/BilalMukhtar/FIFA-Rating-Predictor/blob/main/futbin_understat_combo.ipynb)): used to clean data and match data from both sources
* [`data_cleaning.ipynb`](https://github.com/BilalMukhtar/FIFA-Rating-Predictor/blob/main/data_cleaning.ipynb) ([nbviewer version](https://nbviewer.org/github/BilalMukhtar/FIFA-Rating-Predictor/blob/main/data_cleaning.ipynb)): used to combine cleaned data into one csv file
* [`to_db.ipynb`](https://github.com/BilalMukhtar/FIFA-Rating-Predictor/blob/main/to_db.ipynb) ([nbviewer version](https://nbviewer.org/github/BilalMukhtar/FIFA-Rating-Predictor/blob/main/to_db.ipynb)): used to insert all cleaned data into the database
* [`analysis.nb.html`](https://github.com/BilalMukhtar/FIFA-Rating-Predictor/blob/main/analysis.nb.html) ([source](https://github.com/BilalMukhtar/FIFA-Rating-Predictor/blob/main/analysis.Rmd)): used to insert all cleaned data into the database

### Folders
<details>
  <summary>csv files: raw scraped data and the cleaned/combined data</summary>


  * cleaned_xxxx.csv: Cleaned combination of futbin and understat data
  * futbin_xxxx.csv: Raw data from futbin
  * ustat_xxxx.csv: Raw data from understat
</details>

<details>
  <summary>data repair csvs: csvs used to match player names and clubs</summary>
  
  * check_names.csv: Match names manually/with fuzzy matching between understat and futbin
  * fix_club_ids.csv: Stores ids to match clubs between data sources
  * fix_name_ids: Stores ids to match names between data sources
</details>

<details>
  <summary>sql files: file to create database with correct constraints</summary>

  * SoccerDB.sql: Contains the definitions for the database
</details>

## Database
Based on the following diagram, the goal is to expand the project to also contain data from teams which may improve the current predictions along with allowing for future projects/analysis (Click on the image for an interactive view)
<br></br>
[![alttext](https://github.com/BilalMukhtar/FIFA-Rating-Predictor/blob/main/imgs/soccer_db_png.png)](https://drawsql.app/teams/bilals-team-1/diagrams/soccerdb/embed)

## Predictions
Below are the predictions for the 10 highest rated players in FIFA 23 (The rest are availible in [`predictions.csv`](https://github.com/BilalMukhtar/FIFA-Rating-Predictor/blob/main/predictions.csv)):
|                  Name                  |FIFA 23|           Regression         |Classification|
|:--------------------------------------:|:-----:|:----------------------------:|:------------:|
|Kevin De Bruyne                         |91     |87.6428833333333              |91            |
|Robert Lewandowski                      |91     |88.0882                       |91            |
|Karim Benzema                           |91     |87.7432666666666              |91            |
|Lionel Messi                            |91     |88.8372666666667              |91            |
|Kylian Mbappé                           |91     |88.8922                       |91            |
|Cristiano Ronaldo                       |90     |84.8810166666667              |85            |
|Virgil van Dijk                         |90     |86.5171666666667              |90            |
|Mohamed Salah                           |90     |88.15725                      |89            |
|Thibaut Courtois                        |90     |86.1696333333333              |90            |
|Manuel Neuer                            |90     |85.04305                      |90            |



## Data Sources
* [futbin.com](futbin.com) (FIFA/EAFC Data)
* [understat.com](understat.com) (Player Data)
