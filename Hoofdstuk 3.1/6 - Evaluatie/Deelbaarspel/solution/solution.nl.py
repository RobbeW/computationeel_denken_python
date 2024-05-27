import random

# Initialiseer de teller voor correcte antwoorden
score = 0

for i in range(3):
    # Genereer een willekeurig getal tussen 20 en 50
    getal = random.randint(20, 50)
    print(f"Het getal is {getal}")
    
    # Vraag de gebruiker naar het kwadraat van het getal
    deler = int(input("Geef een deler in: "))

    # Controleer of het antwoord correct is
    if getal % deler == 0:
        print("Juist!")
        if deler != 1 and deler != getal:
            score = score + 2
        else:
            score = score + 1
    else:
        print("Dit is geen deler!")

# Print de totaalscore van de gebruiker
print(f"Score: {score}")
