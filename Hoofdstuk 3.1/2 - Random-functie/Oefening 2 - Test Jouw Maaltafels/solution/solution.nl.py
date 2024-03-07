import random

# Variabele om de score van de gebruiker bij te houden
score = 0

# We doen dit vijf keer
for _ in range(5):
    # Genereer twee willekeurige getallen
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Print de getallen naar het scherm
    print("Getal 1:", num1)
    print("Getal 2:", num2)

    # Vraag aan de gebruiker om het product te berekenen
    answer = int(input("Wat is het product van deze twee getallen? "))

    # Controleer het antwoord
    if answer == num1 * num2:
        print("Goed zo!")
        score += 1  # Voeg een punt toe aan de score van de gebruiker
    else:
        print("Dat is niet correct. Het juiste antwoord is", num1 * num2)

# Print de totaalscore van de gebruiker
print("Je totaalscore is", score, "op 5.")
