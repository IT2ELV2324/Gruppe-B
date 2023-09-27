#Branch starter her
def start(): 
    print("Du har gymdag og skal gå på tur til skogen.")
    print("Underveis ser du to menn som går bak deg og virker mistenkelige.")

    while True:
        print("Valg:")
        print("1. Fight dem")
        print("2. Løp")
        print("3. Stå stille")

        valg = input("Hva velger du? (1/2/3): ")

        if valg == '1':
            print("Du prøver å kjempe mot dem...")
            print("Men de er for sterke for deg. Du blir banket, de raner deg og stikker av.")
            break
        elif valg == '2':
            print("Du bestemmer deg for å løpe fra dem. De er raskere enn deg og innhenter deg. Du blir ranet.")
            break
        elif valg == '3':
            print("Du velger å stå stille...")
            print("De nærmer seg deg, og dessverre, de raner deg.")
            break
        else:
            print("Ugyldig valg. Prøv igjen.")

  
