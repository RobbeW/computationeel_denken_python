# Vraag de gebruiker om de waarde van N
N = int(input("Wat is de waarde van N? "))

# Initialiseer het resultaat op 0
resultaat = 0

# Ga door elk getal van 1 tot N
for i in range(1, N+1):
    # Voeg het kwadraat van het huidige getal toe aan het resultaat
    resultaat += i**2

# Print het resultaat
print("Resultaat:", resultaat)