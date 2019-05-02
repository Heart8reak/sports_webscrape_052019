import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

main_url = 'http://www.espn.com/nfl/standings/_/season/2003'

print("Fetching your data...... ")

response = requests.get(main_url)

print(response.status_code)
soup = BeautifulSoup(response.text, 'lxml')

table = soup.find('table')
rows = table.find_all('tr')

rows = iter(rows)
header_1 = [td.text for td in next(rows).find_all('td') if td.text]
header_2 = [td.text for td in next(rows).find_all('td') if td.text]
header = header_1[:2] + header_2 + header_1[-2:]

print(header)
for row in rows:
    data = [td.text for td in row.find_all('td') if td.text]
    print(data)
 
print(rows)


