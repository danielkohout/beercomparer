import sys

from bs4 import BeautifulSoup
import requests

# Abfrage der zu vergleichenden Städte
city1 = input('Stadt 1: ').strip()
city2 = input('Stadt 2: ').strip()

# Anfrage mit den Parametern an Numbeo. Die Parameter übergibt requests selbst, damit
# Umlaute und Leerzeichen in Städtenamen korrekt kodiert werden.
url = 'https://www.numbeo.com/cost-of-living/compare_cities.jsp'
params = {
    'country1': 'Germany',
    'country2': 'Germany',
    'city1': city1,
    'city2': city2,
    'tracking': 'getDispatchComparison',
}

try:
    resPage = requests.get(url, params=params, timeout=10)
    resPage.raise_for_status()
except requests.RequestException as fehler:
    sys.exit(f'Numbeo ist nicht erreichbar: {fehler}')

# Die Rückgabe, sprich die HTML Seite wird in der Variable zwischengespeichert
soup = BeautifulSoup(resPage.content, 'html.parser')

# Suche nach dem richtigen Inhalt in diesem Fall einer Tabelle mit einer bestimmten Klasse
table = soup.find('table', attrs={'class': 'data_wide_table new_bar_table cost_comparison_table'})
if table is None:
    sys.exit(f'Für "{city1}" und "{city2}" liefert Numbeo keinen Vergleich. '
             'Stimmen die Städtenamen (meist englisch, etwa Munich)?')

# Die Zeile wird über ihre Bezeichnung gesucht, nicht über ihre Position: Fügt Numbeo eine
# Zeile ein, verschiebt sich alles darunter, und eine feste Nummer liest dann einen anderen
# Preis. Gemeint ist das Bier aus dem Supermarkt, 0,5 l in der Flasche.
BEZEICHNUNG = 'Domestic Beer (0.5 Liter Bottle)'

zeile = next((r for r in table.find_all('tr') if BEZEICHNUNG in r.get_text()), None)
if zeile is None:
    sys.exit(f'Numbeo führt die Zeile "{BEZEICHNUNG}" nicht mehr.')

# Die Zellen der Zeile: Bezeichnung, Preis Stadt 1, Preis Stadt 2, Unterschied
zellen = [z.get_text(strip=True) for z in zeile.find_all('td')]
price1 = zellen[1]
price2 = zellen[2]

# Ausgabe des Resultats
print(f"In {city1} kostet ein Bier (0,5 L, Supermarkt) derzeit: ø {price1} und in {city2} ø {price2}")
