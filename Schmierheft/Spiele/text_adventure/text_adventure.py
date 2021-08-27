frage = input("Willst du ein Spiel mit mir Spielen (ja / nein)  ")

if frage.lower().strip() == "ja":
    frage = input("Du überquerst eine Straße, willst du nach links oder rechts?").lower().strip()
    if frage == "links":
        frage = input("Du triffst auf ein Monster, Möchtest du angreifen oder weg rennen.")

        if frage == "angreifen":
            print("keine gute idee, BAM!!! Du wurdest gefressen")
        else:
            print("Gute entscheidung du kannst dich nochmal retten!")   

            frage = input("Dein Bruder kommt zufällig auf einem Motorad vorbei, Du springst auf und bist weg!") 


    elif frage == "rechts":
        print("Du gehst nach rechts über eine Loch, wleches von einem Brett abgedeckt ist, Du fälls in ein tiefes Loch und bist Lost!!!")

    else:
        print("Du bekommst voll ins Gesicht!")   

else:

    print("Selber schuld, du noob!")

