summe = 0
for feld in range(64):  
    reiskorn = 2**feld
    summe = summe + reiskorn
    print("Feld {}. = {:>30,} Reiskörner und damit instgesamt \
         {:>30,} Reiskorn" .format(feld+1,reiskorn, summe))
gewicht = summe * 0.02 / 1000 /1000
print()
print("wenn ein reiskorn 0,2 gram wiegt, wiegen die gesammten " \
    "Reiskörner {:,.0f} Tonnen".format(gewicht))
print("erstmal")