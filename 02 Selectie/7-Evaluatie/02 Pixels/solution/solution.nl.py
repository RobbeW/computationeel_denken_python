# Vraag de gebruiker om een getal
getal = int(input("Voer een getal in: "))

# Controleer de deelbaarheid door 4 en druk de juiste boodschap af
if getal % 3 == 0:
    print("Het scherm is waarschijnlijk ok.")
else:
    print("Het scherm bevat zeker een defect!")
