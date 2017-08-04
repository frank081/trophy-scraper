import requests
from bs4 import BeautifulSoup

username = input("Enter username. ")
url = "https://psnprofiles.com/"+username
r = requests.get(url, 'html.parser')

soup = BeautifulSoup(r.content, 'html.parser')

games = soup.find('table', id="gamesTable").find_all("tr")
for game in games:
        numTrophiesEarned = int(game.find("span", class_="small-info").find("b").text)
        if numTrophiesEarned > 0:
            print(game.find("a", class_="title").text)
            #print(game.find("span", class_="small-info").find("b").text)
            
	
input("Press Enter to continue...")
