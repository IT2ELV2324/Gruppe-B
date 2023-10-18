#Greinen til Martin starter her
def start():
    print("-------------------------")
    print("Du sendte melding til læreren på teams og får en tommel opp.")
    print("Du føler for å dra ut på et eventyr i stedenfor,\nmen vet ikke om det er en god ide")
    print("Drar du ut på eventyr?")
    print()

    choice = input("ja eller nei: ")
    print()
    if(choice == "ja"):
        eventyr()
    else:
        bli_hjemme()
    

#Sti nr. 1
def eventyr():
    print("-----------------------")
    print("Du dro ut på eventyr uten å si noe til familien din.")
    print("Du tar første fly til Tyskland for å oppleve den rike kulturen.")
    print("Etter en dag får familien din vite dette og vil ha deg hjem")
    print("Drar du hjem?")
    print("")

    choice = input("ja eller nei: ")
    if(choice == "ja"):
        dra_hjem()
    else:
        eventyr_del2()

#Sti nr. 2 
def bli_hjemme():
    print("---------------------")
    print("Du velger å bli hjemme siden du ikke gadd å stikke på eventyr")
    print("Du drar på skolen igjen etter høstferien og livet fortsetter som vanlig")

#Sti nr. 1.1
def eventyr_del2():
    print()
    print("Du flytter til Tyskland og blir værende der resten av livet")
    print("Familien din aksepterer valget ditt etter noen måneder når du blir rik")
    print("De besøker deg jevnlig og er fornøyd med at du fulgte drømmen din")
    print("Du får kone, barn og lever til du blir 127 år gammel")

#Sti nr. 1.2
def dra_hjem():
    print()
    print("Du dro hjem fra Tyskland med første fly mulig")
    print("Familien din ble kjempe skuffet over valget om å dra, og brukte lang tid på å tilgi deg")
    print("Du ender opp med en hyggelig kone og en 8-4 jobb,\nmen for aldri barn.")
    print("Du dør i en alder av 73 år gammel.")