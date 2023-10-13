#Branch starter her                     #BJØRNEN KOMMER!!!
def start():
    """
    dette er starfunksjonen som kjøres i mainen
    """
    print("---------------------")
    print("Du valgte sti 3, det er vist en fin tur å gå!")
    print("Du har nå gått i 2 timer, du er dypt inne i skogen, og du hører en lyd...")
    print("Det er en svartbjørn bak deg! Vil du løpe eller finne en annen løsning?")
    print("\nSvar 1 for å løpe, eller 2 for å finne en annen løsning")

    choice = input("skriv inn dit svar her:")

    if choice == "1":          #hvis spilleren velger 1, skal spilleren prøve å løpe vekk fra bjernen
        print(f"Du valgte å løpe vekk fra bjørnen, men den tar deg igjen og slår deg i ryggen...")
    elif choice == "2":
        print(f"Du valgte å finne en annen løsning, har du lyst til å angripe bjøren med øksen i ryggsekken din? (svar ja eller nei)")
        choice = input("skriv inn ditt svar her:")
        if choice == "ja":
            print("Du slo og drepte bjørnen! Gratulerer, nå kan du spise en god bjørnelunsj!")
        elif choice == "nei":
            print("Du ble spist av bjørnen...")
            print("bedre lykke neste gang")
        else:
            print("ugyldig valg. skriv (ja) for å angripe eller (nei) for ikke")
    else:
        print("Ugyldig valg. Velg 1 for å sparke eller 2 for å slå.")
start()