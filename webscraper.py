import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?")

soup = BeautifulSoup(page.content, 'html.parser')

cases = soup.find(id='main_table_countries_today')

countries = cases.find_all(class_="mt_a")
names = []

count = cases.find_all('td')

casenum = []

for country in countries:
    names.append(country.get_text())

length = int(len(count))
for i in range(length):
    if count[i].find(class_="mt_a"):
        casenum.append(count[i+1].get_text())

master = dict(zip(names, casenum))
print(master)