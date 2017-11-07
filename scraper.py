import requests
from bs4 import BeautifulSoup, element
from datetime import datetime
import dateutil.parser
import sys #for exceptions
from trophy import trophy

#username = input("Enter username. ")
url = "https://psnprofiles.com/trophies/483-burnout-paradise/roughdawg4?trophies=earned"
#url = "https://psnprofiles.com/trophies/1806-ni-no-kuni-wrath-of-the-white-witch/roughdawg4?trophies=earned"
#url = "https://psnprofiles.com/trophies/2482-steamworld-dig/"+username+"?trophies=earned"

def scrapeTrophies(url):
    r = requests.get(url, 'lxml')

    soup = BeautifulSoup(r.content, 'lxml')

    #get all table rows from table containing trophies
    trophies = soup.find("table", class_="zebra").find_all('tr', class_='completed')

    #List of all scraped trophy objects
    trophyList = []

    for currentTrophy in trophies:
        try:
            #table rows with valid trophies will have an associated date. Ignore if none.
            noDate = currentTrophy.find('span', class_="typo-top-date") is None
            if noDate:
                continue
            
            #trophy title
            title = currentTrophy.find_all("a", class_="title")[0].text

            #trophy description
            desc = ''
            if currentTrophy.find('br').text == '':
                brTags = currentTrophy.find_all('br')
                for tag in brTags:
                    if isinstance(tag.next_sibling, element.NavigableString):
                        desc += ''.join(tag.next_sibling)

            #strip away white space
            desc = desc.replace('\r', '')
            desc = desc.replace('\n', '')
            desc = desc.replace('\t', '')

            #date
            try:
                rawDate = currentTrophy.find('span', class_="typo-top-date").text
                time = currentTrophy.find('span', class_="typo-bottom-date").text
                timestamp = dateutil.parser.parse(rawDate + " " + time)
                isoTimestamp = timestamp.isoformat(" ")
            except:
                isoTimestamp = ""

            #Type
            typ = ''
            for img in currentTrophy.find_all('img'):
                if img.has_attr('title'):
                    typ = img['title']

            #image
            imgURL = currentTrophy.find('source')['srcset'].split(' ')[0]
            imgURL = imgURL.replace(',', '')

            #create trophy and add to trophy list
            myTrophy = trophy(title, desc, isoTimestamp, typ, imgURL)
            trophyList.append(myTrophy)
            
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    return trophyList
    #input("Press Enter to continue...")
