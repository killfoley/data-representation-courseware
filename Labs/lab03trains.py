import requests
import csv
from bs4 import BeautifulSoup

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'xml')

# print(soup.prettify())

retrieveTags = ['TrainStatus', 'TrainLatitude', 'TrainLongitude', 'TrainCode', 'TrainDate', 'PublicMessage', 'Direction']

with open('week3_trains.csv', mode='w') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    listings = soup.findAll("objTrainPositions")
    for listing in listings:
        lat = float(listing.TrainLatitude.string)
        if lat < 53.4:
            entryList = []    
            for Tag in retrieveTags:
                entryList.append(listing.find(Tag).string)
            train_writer.writerow(entryList)
