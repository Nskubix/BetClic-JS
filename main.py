import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = "https://onefootball.com/en/competition/premier-league-9/fixtures"
page = requests.get(url)

soup = BeautifulSoup(page.text,"html.parser")

all_teams = soup.find_all("span", class_="SimpleMatchCardTeam_simpleMatchCardTeam__name__7Ud8D")
all_scores = soup.find_all("span",class_="SimpleMatchCardTeam_simpleMatchCardTeam__score__UYMc_")

counter = 0
fi = 0
fixtures = {}
for team in all_teams:
    if(counter == 0):
        fixtures[fi] = []
        fixtures[fi].append(team.text)
        counter+=1
    elif(counter == 1):
        fixtures[fi].append(team.text)
        counter = 0
        fi += 1
counter = 0
fi = 0
for score in all_scores:
    if(counter == 0):
        fixtures[fi].append(score.text)
        counter+=1
    elif(counter == 1):
        fixtures[fi].append(score.text)
        counter = 0
        fi += 1

def get_fixtures(num):
    arr = []
    for i in range(num):
        arr.append(fixtures[i])
    return arr

with open("fixtures.csv","w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for fixture in get_fixtures(30):
        writer.writerow(fixture)

