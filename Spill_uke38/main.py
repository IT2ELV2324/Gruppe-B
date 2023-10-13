
import time
from player import *
import branch.jeffer as jeffer
import branch.martin as martin
import branch.oskar as oskar
import branch.simen as simen
import branch.sondre as sondre


SLEEP_TIME = 0.75

start_liste = ["1. Jeg ser to mystiske menn komme mot meg",
               "2. Jeg sender melding til læreren og skriver at jeg er syk",
               "3. Jeg ser en bjørn foran meg",
               "4. Jeg merker jeg må pisse",
               "5. Jeg går tur meg gruppen min",
               "6. Jeg ser et minefelt?"]

spiller = Player(input("Skriv inn navn for å starte eventyret: "))
print("Velkommen", spiller.name)



def introduction_story():
    print("Det er gym fagdag og du skal på tur med skole gruppen din.")
    time.sleep(SLEEP_TIME) 
    print("Du vet ikke helt om du har lyst til dette")
    time.sleep(SLEEP_TIME)

    input("Trykk enter for å fortsette.")
    print()
    print("Du har nå muligheten til å velge hva du vil gjøre.")
    time.sleep(SLEEP_TIME)
    print()
    print()
    
def minefelt():
    print("Du tråkket på et minefelt, gameover!")

def start_game():
    introduction_story()
    
    for i in start_liste:
        print(i)
        time.sleep(SLEEP_TIME)

    choice = input("Skriv tall mellom 1-6 for å velge sti: ")

    if choice == '1':
        jeffer.start()
    elif choice == '2':
        martin.start()
    elif choice == '3':
        oskar.start()
    elif choice == '4':
        simen.start()
    elif choice == '5':
        sondre.start()
    else:
        minefelt()

start_game()

print()
print(f"{spiller.name}, du endte opp med {spiller.xp} XP!")