import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_players(year: int, out=False, count=10, **kwargs):
    page_no = 0

    players = pd.DataFrame(columns = ['name', 'pos', 'card_id', 'year', 'link'])
    
    additional = ''
    
    for key in kwargs:
        additional = additional + '&' + key + '=' + str(kwargs.get(key))

    valid = True

    while valid:
        page_no += 1
        url = f'https://www.futbin.com/{year}/players?page={page_no}' + additional
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(url, headers=headers)
        soup = BeautifulSoup(result.content, 'html.parser')
        ply = soup.find_all("a", {"class": "player_name_players_table get-tp"})
        pos = soup.find_all("div", {"class": "font-weight-bold"})
        
        if ply:
            for j in range(len(ply)):
                players = pd.concat([pd.DataFrame([[ply[j].text, pos[j].text, ply[j].get('data-site-id'), ply[j].get('data-year'), ply[j].get('href')]], columns=players.columns), players], ignore_index=True)
        else:
            valid = False
            
        if out and page_no % count == 0:
            print(page_no)
            
        time.sleep(2)

    return players

def get_stats(players: pd.DataFrame, out=False, count=100):
    links = players['link']
    position = players['pos']

    stats = pd.DataFrame(columns = ['player_id', 'card_id', 'rating', 'pac', 'acceleration', 'sprint_speed', 'sho', 'positioning', 'finishing', 'shot_power', 'long_shots', 
                                    'volleys', 'penalties', 'pas', 'vision', 'crossing', 'fk_accuracy', 'short_passing', 'long_passing', 'curve', 'dri', 'agility', 'balance',
                                    'reactions', 'ball_control', 'dribbling', 'composure', 'def', 'interceptions', 'heading_acc', 'def_awareness', 
                                    'standing_tackle', 'sliding_tackle', 'phy', 'jumping', 'stamina', 'strength', 'aggression', 'gk_diving', 'gk_handling', 'gk_kicking',
                                    'gk_reflexes', 'gk_speed', 'gk_positioning'])

    for i in range(len(links)):
        url = f'https://www.futbin.com{links[i]}'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(url, headers=headers)
        soup = BeautifulSoup(result.content, 'html.parser')
        rating = soup.find("div", {"class": "pcdisplay-rat"})
        ids = soup.find("div", {"id": "page-info"})
        stat_tab = soup.find("div", {"class": "card-body"})
        ss = stat_tab.find_all("div", {"class": "stat_val"})
        
        if ss and position[i] != 'GK':
            stats = pd.concat([pd.DataFrame([[ids.get("data-baseid"), ids.get('data-id'), rating.text, ss[1].text, ss[3].text, ss[5].text, ss[7].text, ss[9].text,
                                            ss[11].text, ss[13].text, ss[15].text, ss[17].text, ss[19].text, ss[21].text, ss[23].text, ss[25].text,
                                            ss[27].text, ss[29].text, ss[31].text, ss[33].text, ss[35].text, ss[37].text, ss[39].text, ss[41].text, ss[43].text,
                                            ss[45].text, ss[47].text, ss[49].text, ss[51].text, ss[53].text, ss[55].text, ss[57].text, ss[59].text,
                                            ss[61].text, ss[63].text, ss[65].text, ss[67].text, ss[69].text, None, None, None, None, None, None]], columns=stats.columns), stats], ignore_index=True)            
        else:
            stats = pd.concat([pd.DataFrame([[ids.get("data-baseid"), ids.get('data-id'), rating.text, None, None, None, 
                                                None, None, None, None, None, None, None, None, None, None,
                                                None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                                                None, None, None, None, None, None, None, None, ss[1].text, ss[5].text, ss[9].text, 
                                                ss[13].text, ss[17].text, ss[21].text]], columns=stats.columns), stats], ignore_index=True)

    if out and i % count == 0:
            print(i)
    
    return stats