import matplotlib.pyplot as plt
summe = 0
feldListe = []

for feld in range(64):  
    reiskorn = 2**feld
    feldListe.append(reiskorn)
    summe += reiskorn
    print(f"Feld {feld+1}. = {reiskorn:>30,} Reiskörner und damit instgesamt" \
         f"{summe:>30,} Reiskörner")
gewicht = summe * 0.02 / 1000 /1000
print()
print("wenn ein reiskorn 0,2 gram wiegt, wiegen die gesammten " \
   f"Reiskörner {gewicht:,.0f} Tonnen")
print()
print(feldListe)

plt.plot(feldListe)
plt.show()