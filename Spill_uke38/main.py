
import branch.jeffer as jeffer
import branch.martin as martin
import branch.oskar as oskar
import branch.simen as simen
import branch.sondre as sondre

def introduction_story():

def start_game():
    introduction_story()

    choice = input()

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

start_game()