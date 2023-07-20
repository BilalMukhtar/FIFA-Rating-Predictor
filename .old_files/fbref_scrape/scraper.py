from bs4 import BeautifulSoup
import requests, time
import pandas as pd
import numpy as np

url = 'https://fbref.com/en/comps/Big5'
yearStart = 2020
yearEnd = 2021
valid = True

headers = {
    'Season': [], 'Overall Rank': [], 'Team': [],
    'Country': [], 'League Rank': [], 'Matches Played': [],
    'Wins': [], 'Draws': [], 'Losses': [], 'Goals For': [],
    'Goals Against': [], 'Goal Difference': [], 'Points': [],
    'Points Per Match': [], 'Expected Goals': [],
    'Expected Goals Against': [], 'Expected Goal Difference': [],
    'Expected Goal Difference Per Match': []}

df = pd.DataFrame(data=headers)

while (yearStart >= 1995):
    time.sleep(5) # Avoid bot prevention
    
    yearCombo = str(yearStart) + '-' + str(yearEnd) 
    r = requests.get(url + '/' + yearCombo + '/' + yearCombo + '-Big-5-European-Leagues-Stats')
    soup = BeautifulSoup(r.content, 'html.parser')
    parsed_table = soup.find('table')

    for i,row in enumerate(parsed_table.find_all('tr')[1:]):
        ovrRank = row.find('th').get_text()
        name = row.find('td', attrs={'data-stat': 'squad'}).a.get_text()
        country = row.find('td', attrs={'data-stat': 'country'}).span.get_text()
        lgRank = row.find('td', attrs={'data-stat': 'rank'}).get_text()
        mp = row.find('td', attrs={'data-stat': 'games'}).get_text()
        w = row.find('td', attrs={'data-stat': 'wins'}).get_text()
        d = row.find('td', attrs={'data-stat': 'draws'}).get_text()
        l = row.find('td', attrs={'data-stat': 'losses'}).get_text()
        gf = row.find('td', attrs={'data-stat': 'goals_for'}).get_text()
        ga = row.find('td', attrs={'data-stat': 'goals_against'}).get_text()
        gd = int(gf) - int(ga)
        pts = row.find('td', attrs={'data-stat': 'points'}).get_text()
        ppg = row.find('td', attrs={'data-stat': 'points_avg'}).get_text()
        if(yearStart >= 2017): 
            xgf = row.find('td', attrs={'data-stat': 'xg_for'}).get_text()
            xga = row.find('td', attrs={'data-stat': 'xg_against'}).get_text()
            xgd = float(xgf) - float(xga)
            xgdpm = xgd / float(mp)
        else:
            xgf = np.nan
            xga = np.nan
            xgd = np.nan
            xgdpm = np.nan

        df.loc[len(df.index)] = [
            yearCombo, ovrRank, name, country, lgRank, 
            mp, w, d, l, gf, ga, gd, pts, ppg, xgf, xga, xgd, xgdpm
            ]

    yearStart -= 1
    yearEnd -= 1


df.to_csv("out.csv", index=False)



