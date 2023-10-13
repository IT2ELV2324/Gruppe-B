#Branch starter her
import sys
import os

# Get the current script's directory (your_script.py's directory)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory
parent_dir = os.path.dirname(current_dir)
# Add the parent directory to the Python path
sys.path.append(parent_dir)

from player import *

valg_sondre=""

def myr():
    print(f"{spiller.name} begynte å gå på myren. Plutselig ga myren etter, og hele deg ble våt. {spiller.name} har nye sokker, men resten av klærne dine er våte. {spiller.name} er kald og klærne dine er tunge på grunn av vann. {spiller.name} kommer deg over. {spiller.name} vurderer å slå leier for å slå leier for å varme deg. {spiller.name} har ikke ved, så {spiller.name} må sanke ved.")
    try:
        valg_sondre=input("Slår {spiller.name} leir?(y/n)\n")
        valg_sondre=valg_sondre.lower()
        if valg_sondre=="y":
            print("{spiller.name} fikk samlet ved, men den var våt og det tok ikke fyr. {spiller.name} var for kald og sliten til å fortsette. {spiller.name} døde")
        elif valg_sondre=="n":
            print("Selv om {spiller.name} var kald, så forsatte {spiller.name} å gå. {spiller.name} møtte på en bil i skogen, som kjørte deg til T-banen. {spiller.name} kom hjem og koste deg i høstferien")
        else:
            print("Svaret er ikke y eller n")
            raise ValueError
    except:
        print("Inputen ble ikke akseptert")

def sti():
    print("{spiller.name} går på stien i 5km og kommer til en seter. Vil {spiller.name} ta deg en bolle?")
    try:
        valg_sondre=input("Vil {spiller.name} ta deg en bolle?(y/n)\n")
        valg_sondre=valg_sondre.lower()
        if valg_sondre=="y":
            print("Bollen er veldig dyr, og {spiller.name} har ikke nok penger. {spiller.name} kan vaske eller løpe.")
            valg_sondre=input("Blir {spiller.name} igjen og vasker?(y/n)\n")
            valg_sondre=valg_sondre.lower()
            if valg_sondre=="y":
                print("{spiller.name} ble der i fem timer, men {spiller.name} kom deg hjem")
            elif valg_sondre=="n":
                print("{spiller.name} løp. En ansatte fanget deg. Politiet kom å hentet deg, og {spiller.name} havnet i fengsel. {spiller.name} koste deg på Bastøy og ble der resten av livet.")
            else:
                print("Svaret er ikke y eller n")
                raise ValueError
        elif valg_sondre=="n":
            print("{spiller.name} gikk videre, men kom deg til T-banen sulten.")
        else:
            print("Svaret er ikke y eller n")
            raise ValueError
    except:
        print("Inputen ble ikke akseptert")
    else:
        print("Turen er over")
        

def start():
    print(f"{spiller.name} valgte sti 5. {spiller.name} endte med å gå 5km. {spiller.name} er ganske sliten. Foran deg ser {spiller.name} en 10 meter høy fjellvegg, en stor myr og en sti. Hva vil {spiller.name}?")
    try:
        valg_sondre=input("Skriv \"F\" for fjell, \"M\" for myr, \"S\" for sti.\n")
        valg_sondre=valg_sondre.lower()
        if valg_sondre == "f":
            print(f"{spiller.name} begynte klatre. {spiller.name} klarte å klatre fem meter opp, men {spiller.name} hadde ikke med deg noe klarteutstyr og {spiller.name} mistet grepet ditt. {spiller.name} falt ned å døde")
        elif valg_sondre == "m":
            myr()
        elif valg_sondre == "s":
            sti()
    except:
        print("Inputen ble ikke akseptert")