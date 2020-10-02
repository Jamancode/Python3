import requests
#print(requests)
r = requests.get('http://google.com') # fragt eine webseite an

#print(r.text)                         # gibt inhalt der Datei aus, hier den html text der seite aus.

f = open('google.html','w')           # öffnet datein mit namen google.html
f.write(r.text)                       # schreibt die abfrage, hier ein text von dem request.get (r.text) in die geöffnete datei.

f.flush()                             # rest aus dem buffer wird hier in die datei geschrieben
f.close()                             # hier wird die datei geschlossen

s = 0

while s < 100: #  eine schleife wie oft  
    get_parameters ={'q':'irgendwas,'start':str(s)}  # eingabe in google suchfenster, drück start
    r2 = requests.get('http://www.google.de/search',get_parameters) #mach das

    print(r2.text)

    f = open('google_suche_'+str(s)+'.html','w')
    f.write(r2.text)

    f.flush()
    f.close()

    s = s + 10
