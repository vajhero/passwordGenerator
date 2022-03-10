import string
import random

plik = open("haslo.txt", "w")

wielkieLitery = list(string.ascii_letters.upper())
maleLitery = list(string.ascii_letters.lower())
cyfry = list(string.digits)
specjalne = list("!@#$%^&*()")

def generujHaslo():
    iloscWielkichLiter = int(input("Podaj ile chcesz wielkich liter"))
    iloscMalychLiter = int(input("Podaj ile chcesz małych liter"))
    iloscCyfr = int(input("Podaj ile chcesz cyfr"))
    iloscSpecjalnych = int(input("Podaj ile chcesz znaków specjalnych"))
    
    hasloWielkieLitery = []
    for i in range(iloscWielkichLiter):
        hasloWielkieLitery.append(random.choice(wielkieLitery))
    
    hasloMaleLitery = []
    for i in range(iloscMalychLiter):
        hasloMaleLitery.append(random.choice(maleLitery))
    
    hasloCyfry = []
    for i in range(iloscCyfr):
        hasloCyfry.append(random.choice(cyfry))
        
    hasloSpecjalne = []
    for i in range (iloscSpecjalnych):
        hasloSpecjalne.append(random.choice(specjalne))
            
    haslo = hasloWielkieLitery + hasloMaleLitery + hasloCyfry + hasloSpecjalne
    random.shuffle(haslo)
    hasloStr = "".join(haslo)
    print(hasloStr)
    plik.write(hasloStr)
    plik.close()

generujHaslo()