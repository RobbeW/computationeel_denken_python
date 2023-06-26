# initialiseer de variabele voor de som
som = 0

# vraag de gebruiker tien keer om een geheel getal
for i in range(10):
    getal = int(input("Voer een geheel getal in: "))
    som += getal  # voeg het ingevoerde getal toe aan de som

# print de som van de getallen
print("De som van de getallen is", som)
