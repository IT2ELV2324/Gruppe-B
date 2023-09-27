#Branch starter her
import time

def m():
    print("--------------------")
def alt():
    m()
    print("1: Ja")
    print("2: Nei")
    valg = input("")
    return valg.lower()
#stier
    
DELAY = 1

list = ["Du valgte 4, du begynner å gå ut i skogen vekk fra stien.", "Plutselig hører du en lyd. Kommer den ovenfra?", "Kanskje burde du gå tilbake til de andre"]
list_1 = ["Du begynner å gå tilbake, lyden synes ikke følge etter deg", "du kommer deg trygt tilbake til stien og får en fet tur"]
list_2 = ["Du står stille, Du blir blendet av et lys ovenfra", "Plutselig begynner du å sveve oppover", "Når du endelig treffer noe som føles som bakke ser du fortsatt ikke klart", "etter noen sekunder tilpasser synet seg, foran deg står en rar skapning", "Hallo kjære jordboer, vi er fra planeten m29", "Vi gjøre noen eksprimenter på deg, ditt offer vil være for universets beste", "Skal du prøve å rømme?"]
list_21 = ["Du dytter karen ned og hopper ut hullet du kom fra", "Du faller i flere sekunder og lander i et tre", "Etter noen sekunder hører du romskipet fly vekk", "du løper tilbake til de andre og forteller hva som skjedde", "Ingen tror på deg"]


def sti1():
    for i in range(len(list_1)):
        print(list_1[i])
        time.sleep(DELAY)
def sti2():
    for i in range(len(list_2)):
        print(list_2[i])
        time.sleep(DELAY)
    valgte2 = alt()
    if valgte2 == "ja":
        sti21()
    elif valgte2 == "nei":
        sti22()

def sti21():
    for i in range(len(list_21)):
        print(list_21[i])
        time.sleep(DELAY)
def sti22():
    print("Du døde")
    
def start():
    for i in range(len(list)):
        print(list[i])
        time.sleep(DELAY)
    valgte = alt()
    if valgte == "ja":
        sti1()
    elif valgte == "nei":
        sti2()

start()