from bs4 import BeautifulSoup
import requests, time
import pandas as pd
import numpy as np
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getTeamList(league, season):
    url = f"https://understat.com/league/{league}/{season}"
    driver.get(url)
    html = driver.page_source

    teams = driver.find_elements("xpath", '//div[@id="leaguechemp"]/table/tbody/tr')
    teamList = []

    for i in teams:
        team = i.find_elements("xpath", './/*')
        curTeam = team[1].text
        teamList.append(curTeam)
        
    return teamList

#######################################################

def getTeamStats(league, season):
    url = f"https://understat.com/league/{league}/{season}"
    driver.get(url)
    html = driver.page_source

    teams = driver.find_elements("xpath", '//div[@id="leaguechemp"]/table/tbody/tr')
    teamList = []

    for i in teams:
        team = i.find_elements("xpath", './/*')
        curTeam = team[1].text
        teamList.append(curTeam)

#######################################################

def getTeamPlayers(team, season):
    url = f"https://understat.com/team/{team}/{season}"
    driver.get(url)
    html = driver.page_source
    
    colList = ["Season", "Team", "Player", "Pos", "Apps", "Min", "G", "A", "Sh90", 
               "KP90", "xG", "xGdiff", "xA", "xAdiff", "xG90", "xA90"] 

    playerdf = pd.DataFrame(columns = colList)

    players = driver.find_elements("xpath", '//div[@id="team-players"]/table/tbody/tr')
    players = players[:len(players) - 1]

    for i in players:
        player = i.find_elements("xpath", './/*')
        player = player[2:]
        curDict = {}
        k = 2
        col = colList[0]
        curDict[col] = season
        col = colList[1]
        curDict[col] = team

        for j in player:
            item = j.text
            col = colList[k]
            if(col == "xG" or col == "xA"):
                if "+" in item:
                    item = item.split("+")
                    curDict[col] = item[0]
                elif "-" in item:
                    item = item.split("-")
                    curDict[col] = item[0]
                else:
                    curDict[col] = item
            else:
                curDict[col] = item
            k += 1

        cur = pd.DataFrame(data=[curDict])
        playerdf = pd.concat([playerdf, cur])
    
    return playerdf

#######################################################

def getLeaguePlayers(league, season):
    teams = getTeamList(league, season)
    teamNum = 0
    
    for i in teams:
        curTeam = getTeamPlayers(teams[teamNum], season)
        
        if(teamNum == 0):
            df = curTeam
        else:
            df = pd.concat([df, curTeam])
            
        teamNum += 1
            
    return df

#######################################################

def getAllPlayers(season):
    leagues = ["EPL", "La_liga", "Bundesliga", "Serie_A", "Ligue_1"]
    leagueNum = 0
    
    for i in legaues:
        curLeague = getLeaguePlayers(leagues[leagueNum], season)
        
        if(teamNum == 0):
            df = curTeam
        else:
            df = pd.concat([df, curLeague])
            
        leagueNum += 1
    
    return df

########################################################

def fullPlayers():
    seasons = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
    seasonNum = 0
    
    for i in legaues:
        curSeason = getLeaguePlayers(seasons[seasonNum])
        
        if(teamNum == 0):
            df = curSeason
        else:
            df = pd.concat([df, curSeason])
            
        seasonNum += 1
    
    return df