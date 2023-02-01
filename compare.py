from bs4 import BeautifulSoup
import requests

city1 = input('Stadt 1: ')
city2 = input('Stadt 2: ')

url = f'https://www.numbeo.com/cost-of-living/compare_cities.jsp?country1=Germany&country2=Germany&city1={city1}&city2={city2}&tracking=getDispatchComparison'
resPage = requests.get(url)
soup = BeautifulSoup(resPage.content, 'html.parser')

table = soup.find('table',attrs={'class':'data_wide_table new_bar_table cost_comparison_table'})
rows = table.find_all('tr')

beer_data = rows[26].text.split()
price1 = beer_data[5]
price2 = beer_data[7]

print(f"In {city1} kostet Bier derzeit: ø {price1}€ und in {city2} ø {price2}€")


