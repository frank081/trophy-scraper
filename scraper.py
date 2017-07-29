import requests
from bs4 import BeautifulSoup

username = input("Enter username. ")
url = "https://psnprofiles.com/trophies/1806-ni-no-kuni-wrath-of-the-white-witch/"+username
r = requests.get(url, 'html.parser')

soup = BeautifulSoup(r.content, 'html.parser')

trophies = soup.find_all("tr", class_="completed")
for trophy in trophies:
    print(trophy.find_all("a", class_="title")[0].text)
    desc = ''.join(trophy.find('br').next_siblings)
    desc = desc.replace('\r', '')
    desc = desc.replace('\n', '')
    desc = desc.replace('\t', '')
    print(desc)
    
input("Press Enter to continue...")
