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
    
DELAY = 2

list = ["Du valgte 4, du begynner å gå ut i skogen vekk fra stien.", "Plutselig hører du en lyd. Kommer den ovenfra?", "Kanskje burde du gå tilbake til de andre"]
list_2 = ["Du begynner å gå tilbake, lyden synes ikke følge etter deg", "du kommer deg trygt tilbake til stien og får en fet tur"]
list_3 = ["Du står stille, Du blir blendet av et lys ovenfra", "Plutselig begynner du å sveve oppover", "Når du endelig treffer noe som føles som bakke ser du fortsatt ikke klart", "etter noen sekunder tilpasser synet seg, foran deg står en rar skapning", "Hallo kjære jordboer, vi er fra planeten m29", "Vi gjøre noen eksprimenter på deg, ditt offer vil være for universets beste", "Skal du prøve å rømme?"]


def sti1():
    for i in range(len(list_2)):
        print(list_2[i])
        time.sleep(DELAY)
def sti2():
    for i in range(len(list_3)):
        print(list_3[i])
        time.sleep(DELAY)
    alt()
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