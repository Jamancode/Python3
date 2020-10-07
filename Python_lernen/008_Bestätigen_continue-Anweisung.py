while True:
    print ('Wer bist du?')
    name = input()
    if name != 'Jaman':
        continue
    print ('Was geht bei dir so, Jaman? Wie lautet das passwort? (Es hat nur ein Rad.)')
    passwort = input()
    if passwort == 'Einrad':
        break
print('Komm gern rein!')