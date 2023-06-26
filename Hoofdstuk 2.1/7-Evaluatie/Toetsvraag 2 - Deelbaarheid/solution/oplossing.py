# Vraag de gebruiker om een getal
getal = int(input("Voer een getal in: "))

# Controleer de deelbaarheid door 4 en druk de juiste boodschap af
if getal % 4 == 0:
    print("Scherm is in orde!")
else:
    print("Scherm bevat een defect!")
