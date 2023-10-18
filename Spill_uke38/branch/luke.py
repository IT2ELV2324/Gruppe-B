import random

def return_to_teacher():
    print("\nDu går tilbake for å varsle læreren om minefeltet.")
    print("Læreren tar umiddelbare skritt for å sørge for at alle er trygge.")
    print("Turen fortsetter uten problemer.")
    print("Takk for at du tok det trygge valget!")
    
def attempt_crossing_minefield():
    success = random.choice([True, False])

    if success:
        print("\nDu fant en trygg vei gjennom minefeltet! Du er trygg.")
        print("Gratulerer, du har overlevd!")
    else:
        print("\nDessverre, du satte av en mine og har blitt såret.")
        print("Spillet er over. Prøv igjen senere.")
        
def explore_minefield():
    print("\nDu står foran et farlig minefelt.")
    print("Hva vil du gjøre?")
    print("1. Prøv å finne en trygg vei gjennom minefeltet.")
    print("2. Gå tilbake og varsle læreren om minefeltet.")

    choice = input("Skriv inn valget ditt (1/2): ")

    if choice == "1":
        attempt_crossing_minefield()
    elif choice == "2":
        return_to_teacher()
    else:
        print("Ugyldig valg. Prøv igjen.")
        explore_minefield()
        
def start():
    print("Plutselig ser du et minefelt foran deg.")
    print("Du må ta en beslutning for å komme trygt gjennom. Lykke til!")
    explore_minefield()

if __name__ == "__main__":
    start()
