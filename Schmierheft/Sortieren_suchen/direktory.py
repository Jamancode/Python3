#   ein "Dictionary" oder deutsch "Verzeichnis" ist sehr schnell, verwaltet Listen oder einträge zu eine "Schlagwort", 
#   es benötigt immer.   dir ={key:value}     schlüsselwert:inhaltswert
#  erklärung im video: https://youtu.be/uZsFGyhsPLE?t=880

print()
print("Wir spielen etwas mit listen und verzeichnisen herrum.")
print()

dir1 = {'Karl':[42, 32, 21], 'Sophie':[32, 64, 128]}
dir2 = {'deep':[1337, 815, 1234], 'deeper':[3, 7, 12]}
liste1 = [41,63,92]

print(dir1)
print(liste1 + (dir1['Sophie']))
print()
print(liste1[1])
print(dir1['Karl'])
print()
print(dir1['Karl'][2])