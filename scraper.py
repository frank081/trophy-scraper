import requests
from bs4 import BeautifulSoup

username = input("Enter username. ")
url = "https://psnprofiles.com/trophies/2482-steamworld-dig/"+username
r = requests.get(url, 'html.parser')

soup = BeautifulSoup(r.content, 'html.parser')

trophies = soup.find_all("tr", class_="completed")
for trophy in trophies:
    try:
        #skip the banner that appears when a game has been completed.
        #the title text is used to differentiate it from the trophies.
        if trophy.find_all("a", class_="title")[0].text != username:
            #trophy title
            print(trophy.find_all("a", class_="title")[0].text)

            desc = ''
            #other trophies
            if trophy.find('br').text == '':
                brTags = trophy.find_all('br')
                for tag in brTags:
                    desc += ''.join(tag.next_sibling)
            #platinium
            else:
                desc += trophy.find('br').text
            
            #strip away white space
            desc = desc.replace('\r', '')
            desc = desc.replace('\n', '')
            desc = desc.replace('\t', '')
            print(desc)
    except:
        pass
    
input("Press Enter to continue...")
