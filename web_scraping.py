import urllib.request
from bs4 import BeautifulSoup
import requests


wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

page = requests.get(wiki)
soup= BeautifulSoup(page.content, 'html5lib')

#print(soup.prettify())

print(soup.title)
links = soup.find_all('a')
print(len(links))

tables = soup.find_all('table')
print(len(tables))

for t in tables:
    #print(t.prettify())
    print()

table1 = tables[2]
#print(table1.prettify())
print(table1.attrs)

tb = soup.find('table', attrs= {'class': ['wikitable', 'sortable', 'plainrowheaders']})
print(tb.attrs)

#print(soup.table.attrs)

print(soup.name)

text = soup.get_text()




