from bs4 import BeautifulSoup
import requests

# Abfrage der zu vergleichenden Städte
city1 = input('Stadt 1: ')
city2 = input('Stadt 2: ')

# Anfrage mit den Parametern an Numbeo
url = f'https://www.numbeo.com/cost-of-living/compare_cities.jsp?country1=Germany&country2=Germany&city1={city1}&city2={city2}&tracking=getDispatchComparison'
resPage = requests.get(url)

# Die Rückgabe, sprich die HTML Seite wird in der Variable zwischengespeichert
soup = BeautifulSoup(resPage.content, 'html.parser')

# Suche nach dem richtigen Inhalt in diesem Fall einer Tabelle mit einer bestimmten Klasse
table = soup.find('table',attrs={'class':'data_wide_table new_bar_table cost_comparison_table'})
rows = table.find_all('tr')

# DIe gefundene Tabelle wird zerpflückt und in Variablen gespeichert
beer_data = rows[26].text.split()
price1 = beer_data[5]
price2 = beer_data[7]

# Ausgabe des Resultats
print(f"In {city1} kostet Bier derzeit: ø {price1}€ und in {city2} ø {price2}€")


