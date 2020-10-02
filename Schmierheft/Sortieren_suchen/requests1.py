import requests
#print(requests)
r = requests.get('http://google.com') # fragt eine webseite an

#print(r.text)                         # gibt inhalt der Datei aus, hier den html text der seite aus.

f = open('google2.html','w')           # öffnet datein mit namen google.html
f.write(r.text)                       # schreibt die abfrage, hier ein text von dem request.get (r.text) in die geöffnete datei.

f.flush()                             # rest aus dem buffer wird hier in die datei geschrieben
f.close()                             # hier wird die datei geschlossen


