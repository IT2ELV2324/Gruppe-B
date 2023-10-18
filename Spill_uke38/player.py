import random

class Player:
    def __init__(self, name):
        """ This is a class for defining names of players. This class also randomly selects a xp for each player """
        self.name = name
        self.xp = random.randint(20, 100)

spiller = Player(input("Skriv inn navn for å starte eventyret: ")) #Setter spiller navn
print("Velkommen", spiller.name)