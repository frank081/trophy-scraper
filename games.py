import requests
from bs4 import BeautifulSoup

def createSoup(username, page):
    r = requests.get("https://psnprofiles.com/{}?ajax=1&completion=all&order=last-played&pf=all&page={}".format(username,page), 'html.parser')
    response=r.json()['html']
    soup=BeautifulSoup(response, 'html.parser')
    return soup

username = input("Enter username. ")
page = 1

soup = createSoup(username, page)
result = soup.find(text="No games found")

if result is None:
    games = soup.find_all('tr')
    for game in games:
        try:
            numTrophiesEarned = int(game.find("span", class_="small-info").find("b").text)
            if numTrophiesEarned > 0:
                print(game.find("a", class_="title").text)
        except:
            pass
    page = page + 1
    soup = createSoup(username, page)
    result = soup.find(text="No games found")


