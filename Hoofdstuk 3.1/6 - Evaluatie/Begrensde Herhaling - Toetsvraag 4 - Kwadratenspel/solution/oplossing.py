import random

# Initialiseer de teller voor correcte antwoorden
correcte_antwoorden = 0

# Itereer over een reeks van 10 getallen (voor 10 vragen)
for i in range(10):
    # Genereer een willekeurig getal tussen 1 en 10
    getal = random.randint(1, 10)

    # Vraag de gebruiker naar het kwadraat van het getal
    antwoord = int(input("Wat is het kwadraat van " + str(getal) + "? "))

    # Controleer of het antwoord correct is
    if antwoord == getal ** 2:
        print("Goed zo!")
        correcte_antwoorden += 1
    else:
        print("Fout, het juiste antwoord is", getal ** 2)

# Print de totaalscore van de gebruiker
print("Je totaalscore is:", correcte_antwoorden, "/10.")
