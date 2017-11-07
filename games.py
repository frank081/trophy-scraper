import requests
from bs4 import BeautifulSoup
import scraper
from game import game
import jsonpickle

def createSoup(username, page):
    r = requests.get("https://psnprofiles.com/{}?ajax=1&completion=all&order=last-played&pf=all&page={}".format(username,page), 'html.parser')
    response=r.json()['html']
    soup=BeautifulSoup(response, 'html.parser')
    return soup

username = input("Enter username. ")
page = 1

soup = createSoup(username, page)
result = soup.find(text="No games found")

#list of games scraped
gameList = []

while result is None:
    #print(page)
    games = soup.find_all('tr')
    for eachGame in games:
        try:
            numTrophiesEarned = int(eachGame.find("span", class_="small-info").find("b").text)
            if numTrophiesEarned > 0:
                #Title
                title = eachGame.find("a", class_="title").text
                print(title)
                
                #Link
                link_text = '' 
                for a in eachGame.find_all('a', href=True): 
                    if a.text.strip(): 
                        link_text = a['href']
                print('\tLink: ' + link_text)
                full_url = "https://psnprofiles.com" + link_text + "?trophies=earned"

                #scrape trophies with url and add all trophies a game object
                gameObj = game(title)
                trophies = scraper.scrapeTrophies(full_url)
                for trophy in trophies:
                    gameObj.addTrophy(trophy)
                gameList.append(gameObj)
        except:
            pass
    page = page + 1
    soup = createSoup(username, page)
    result = soup.find(text="No games found")

#Export game list and trophies to json
file = open("pickletest.txt","w")
file.write(jsonpickle.encode(gameList))
file.close()

