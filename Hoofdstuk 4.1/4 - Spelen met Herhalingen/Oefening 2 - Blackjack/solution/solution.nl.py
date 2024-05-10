import random

# Geef de gebruiker twee willekeurige getallen tussen 1 en 10
kaart_1 = random.randint(1, 10)
kaart_2 = random.randint(1, 10)
print("Je kreeg kaarten", kaart_1, "en", kaart_2)

# Bereken de som van de twee getallen
som = kaart_1 + kaart_2

# Vraag of de gebruiker nog een kaart wil
keuze = input("Wil je nog een kaart? ")

# Zolang de gebruiker een kaart wil en de som niet groter is dan 21
while keuze == 'ja' and som <= 21:
    # Genereer een nieuwe kaart en verhoog de som
    nieuwe_kaart = random.randint(1, 10)
    som += nieuwe_kaart

    # Print de nieuwe kaart en de huidige som
    print("De nieuwe kaart is:", nieuwe_kaart)
    print("De som bedraagt nu:", som)

    # Als de som nog steeds niet groter is dan 21, vraag of de gebruiker nog een kaart wil
    if som < 21:
        keuze = input("Wil Je nog een kaart? ")

# Als het spel is afgelopen
if som == 19:
    print("Je wint 2 euro!")
elif som == 20:
    print("Je wint 5 euro!")
elif som == 21:
    print("Je wint 10 euro!")
else:
    print("Je verliest!")
