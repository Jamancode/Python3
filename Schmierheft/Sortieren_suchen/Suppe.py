
import requests
from bs4 import BeautifulSoup


html = requests.get('https://taramar.de/fashion/kinder/hosen/641/kinderhose-santos-in-gruen?c=59')

soup = BeautifulSoup(html.text,'lxml')
f = open('tara.html','w')           # öffnet datein mit namen google.html
f.write(html.text)                       # schreibt die abfrage, hier ein text von dem request.get (r.text) in die geöffnete datei.

f.flush()                             # rest aus dem buffer wird hier in die datei geschrieben
f.close()                             # hier wird die datei geschlossen


for size in soup.find_all('a',class_='box'):
    print(size)
 