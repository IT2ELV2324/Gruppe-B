#Branch starter her
valg_sondre=""

def myr():
    print(f"Du begynte å gå på myren. Plutselig ga myren etter, og hele deg ble våt. Du har nye sokker, men resten av klærne dine er våte. Du er kald og klærne dine er tunge på grunn av vann. Du kommer deg over. Du vurderer å slå leier for å slå leier for å varme deg. Du har ikke ved, så du må sanke ved.")
    try:
        valg_sondre=input("Slår du leir?(y/n)\n")
        valg_sondre=valg_sondre.lower()
        if valg_sondre=="y":
            print("Du fikk samlet ved, men den var våt og det tok ikke fyr. Du var for kald og sliten til å fortsette. Du døde")
        elif valg_sondre=="n":
            print("Selv om du var kald, så forsatte du å gå. Du møtte på en bil i skogen, som kjørte deg til T-banen. Du kom hjem og koste deg i høstferien")
        else:
            print("Svaret er ikke y eller n")
            raise ValueError
    except:
        print("Inputen ble ikke akseptert")

def sti():
    print("Du går på stien i 5km og kommer til en seter. Vil du ta deg en bolle?")
    try:
        valg_sondre=input("Vil du ta deg en bolle?(y/n)\n")
        valg_sondre=valg_sondre.lower()
        if valg_sondre=="y":
            print("Bollen er veldig dyr, og du har ikke nok penger. Du kan vaske eller løpe.")
            valg_sondre=input("Blir du igjen og vasker?(y/n)\n")
            valg_sondre=valg_sondre.lower()
            if valg_sondre=="y":
                print("Du ble der i fem timer, men du kom deg hjem")
            elif valg_sondre=="n":
                print("Du løp. En ansatte fanget deg. Politiet kom å hentet deg, og du havnet i fengsel. Du koste deg på Bastøy og ble der resten av livet.")
            else:
                print("Svaret er ikke y eller n")
                raise ValueError
        elif valg_sondre=="n":
            print("Du gikk videre, men kom deg til T-banen sulten.")
        else:
            print("Svaret er ikke y eller n")
            raise ValueError
    except:
        print("Inputen ble ikke akseptert")
    else:
        print("Turen er over")
        

def start():
    print(f"Du valgte sti 5. Du endte med å gå 5km. Du er ganske sliten. Foran deg ser du en 10 meter høy fjellvegg, en stor myr og en sti. Hva vil du?")
    try:
        valg_sondre=input("Skriv \"F\" for fjell, \"M\" for myr, \"S\" for sti.\n")
        valg_sondre=valg_sondre.lower()
        if valg_sondre == "f":
            print(f"Du begynte klatre. Du klarte å klatre fem meter opp, men du hadde ikke med deg noe klarteutstyr og du mistet grepet ditt. Du falt ned å døde")
        elif valg_sondre == "m":
            myr()
        elif valg_sondre == "s":
            sti()
    except:
        print("Inputen ble ikke akseptert")