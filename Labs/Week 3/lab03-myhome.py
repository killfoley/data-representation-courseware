# this program will store price and address for properties from the myhome.ie website for Mayo
# inmport packages
import requests
import csv
from bs4 import BeautifulSoup as bs

# set the url
url = 'https://www.property.ie/property-for-sale/mayo/'
page = requests.get(url)

# use beautiful soup to parse the page
soup = bs(page.content, 'html.parser')

# open a file to write the data to
property_file = open('week03propery.csv', mode='w')
property_writer = csv.writer(property_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# find all listings with class = "search_result"
listings = soup.findAll("div", class_="search_result")

# loop through the listings to store price and address
for listing in listings:
    entryList = []
    address = listing.find(class_="sresult_address").find("h2").find("a").text.strip()
    entryList.append(address)
    price = listing.find(class_="sresult_description").find("h3").text.strip()
    entryList.append(price)
    
    property_writer.writerow(entryList)

property_file.close()
    