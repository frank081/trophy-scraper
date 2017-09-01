import requests
from bs4 import BeautifulSoup, element
from datetime import datetime
import dateutil.parser
import sys #for exceptions

username = input("Enter username. ")
#url = "https://psnprofiles.com/trophies/483-burnout-paradise/"+username+"?trophies=earned"
url = "https://psnprofiles.com/trophies/1806-ni-no-kuni-wrath-of-the-white-witch/roughdawg4?trophies=earned"
#url = "https://psnprofiles.com/trophies/2482-steamworld-dig/"+username+"?trophies=earned"
r = requests.get(url, 'lxml')

soup = BeautifulSoup(r.content, 'lxml')

#get all table rows from table containing trophies
trophies = soup.find("table", class_="zebra").find_all('tr', class_='completed')

for trophy in trophies:
    try:
        #table rows with valid trophies will have an associated date. Ignore if none.
        noDate = trophy.find('span', class_="typo-top-date") is None
        if noDate:
            continue
        
        #trophy title
        print(trophy.find_all("a", class_="title")[0].text)

        desc = ''
        #other trophies
        if trophy.find('br').text == '':
            brTags = trophy.find_all('br')
            for tag in brTags:
                if isinstance(tag.next_sibling, element.NavigableString):
                    desc += ''.join(tag.next_sibling)

        #strip away white space
        desc = desc.replace('\r', '')
        desc = desc.replace('\n', '')
        desc = desc.replace('\t', '')
        print("\t" + desc)

        #date
        date = trophy.find('span', class_="typo-top-date").text
        time = trophy.find('span', class_="typo-bottom-date").text
        timestamp = dateutil.parser.parse(date + " " + time)
        isoTimestamp = timestamp.isoformat(" ")
        print("\t" + isoTimestamp)

        #Type
        for img in trophy.find_all('img'):
            if img.has_attr('title'):
                print(img['title'])

        #image
        imgURLs = trophy.find('source')['srcset'].split(' ')
        print(imgURLs[1])
            
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    
input("Press Enter to continue...")
