
import time
import branch.jeffer as jeffer
import branch.martin as martin
import branch.oskar as oskar
import branch.simen as simen
import branch.sondre as sondre

SLEEP_TIME = 1

start_liste = ["Jeg ser to mystiske menn komme mot meg",
               "Jeg sender melding til læreren og skriver at jeg er syk",
               "Jeg ser en bjørn foran meg",
               "Jeg merker jeg må pisse",
               "Jeg går tur meg gruppen min",
               "Jeg ser et minefelt?"]


def introduction_story():
    print("Det er gym fagdag og du skal på tur med skole gruppen din.")
    time.sleep(SLEEP_TIME) 
    print("Du vet ikke helt om du har lyst til dette")
    time.sleep(SLEEP_TIME)
    print("Du har nå muligheten til å velge hva du vil gjøre.")
    time.sleep(SLEEP_TIME)
    
def minefelt():
    print("Gameover")

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