import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_team_list(league, season, driver):
    url = f"https://understat.com/league/{league}/{season}"
    driver.get(url)

    teams = driver.find_elements("xpath", '//div[@id="league-chemp"]/table/tbody/tr')
    team_list = []

    for i in teams:
        team = i.find_elements("xpath", './/*')
        cur_team = team[1].text
        team_list.append(cur_team)
        
    return team_list

#######################################################

def get_team_players(team, season, driver):
    url = f"https://understat.com/team/{team}/{season}"
    driver.get(url)
    
    col_list = ["Season", "Team", "Player", "Pos", "Apps", "Min", "G", "A", "Sh90", 
               "KP90", "xG", "xGdiff", "xA", "xAdiff", "xG90", "xA90"]

    playerdf = pd.DataFrame(columns = col_list)

    players = driver.find_elements("xpath", '//div[@id="team-players"]/table/tbody/tr')
    players = players[:len(players) - 1]

    for i in players:
        player = i.find_elements("xpath", './/*')
        player = player[2:]
        cur_dict = {}
        k = 2
        col = col_list[0]
        cur_dict[col] = season
        col = col_list[1]
        cur_dict[col] = team

        for j in player:
            item = j.text
            col = col_list[k]
            if(col == "xG" or col == "xA"):
                if "+" in item:
                    item = item.split("+")
                    cur_dict[col] = item[0]
                elif "-" in item:
                    item = item.split("-")
                    cur_dict[col] = item[0]
                else:
                    cur_dict[col] = item
            else:
                cur_dict[col] = item
            k += 1

        cur = pd.DataFrame(data=[cur_dict])
        playerdf = pd.concat([playerdf, cur])

    playerdf.astype(int)
    
    return playerdf

#######################################################

def get_league_players(league, season):
    teams = get_team_list(league, season)
    team_num = 0
    
    for i in teams:
        cur_team = get_team_players(teams[team_num], season)
        
        if(team_num == 0):
            df = cur_team
        else:
            df = pd.concat([df, cur_team])
            
        team_num += 1
            
    return df

#######################################################

def get_all_players(season):
    leagues = ["EPL", "La_liga", "Bundesliga", "Serie_A", "Ligue_1"]
    league_num = 0
    
    for i in leagues:
        cur_league = get_league_players(leagues[league_num], season)
        
        if(league_num == 0):
            df = cur_league
        else:
            df = pd.concat([df, cur_league])
            
        league_num += 1
    
    return df

########################################################

def full_players():
    seasons = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
    season_num = 0
    
    for i in seasons:
        cur_season = get_all_players(seasons[season_num])
        
        if(season_num == 0):
            df = cur_season
        else:
            df = pd.concat([df, cur_season])
            
        season_num += 1
    
    return df

########################################################

def get_team_stats(league, season, driver):
    url = f"https://understat.com/league/{league}/{season}"
    driver.get(url)
    
    col_list = ["Season", "Team", "M", "W", "D", "L", "G", "GA", "PTS", 
               "xG", "xGdiff", "xGA", "xGAdiff", "xPTS", "xPTSdiff"]

    teamdf = pd.DataFrame(columns = col_list)

    teams = driver.find_elements("xpath", '//div[@id="league-chemp"]/table/tbody/tr')

    for i in teams:
        team = i.find_elements("xpath", './/*')
        team = team[2:]
        cur_dict = {}
        k = 1
        col = col_list[0]
        cur_dict[col] = season

        for j in team:
            item = j.text
            col = col_list[k]
            if(col == "xG" or col == "xGA" or col == "xPTS"):
                if "+" in item:
                    item = item.split("+")
                    cur_dict[col] = item[0]
                elif "-" in item:
                    item = item.split("-")
                    cur_dict[col] = item[0]
                else:
                    cur_dict[col] = item
            else:
                cur_dict[col] = item
            k += 1

        cur = pd.DataFrame(data=[cur_dict])
        teamdf = pd.concat([teamdf, cur])

    col_list.remove("Team")

    teamdf[col_list]= teamdf[col_list].astype(float)
    
    return teamdf

########################################################

def get_all_teams(season):
    leagues = ["EPL", "La_liga", "Bundesliga", "Serie_A", "Ligue_1"]
    league_num = 0
    
    for i in leagues:
        cur_league = get_team_stats(leagues[league_num], season)
        
        if(league_num == 0):
            df = cur_league
        else:
            df = pd.concat([df, cur_league])
            
        league_num += 1
    
    return df

########################################################

def full_teams():
    seasons = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
    season_num = 0
    
    for i in seasons:
        cur_season = get_all_teams(seasons[season_num])
        
        if(season_num == 0):
            df = cur_season
        else:
            df = pd.concat([df, cur_season])
            
        season_num += 1
    
    return df