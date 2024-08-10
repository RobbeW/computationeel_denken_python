# Vraag de gebruiker om een positief geheel getal in te voeren
getal = int(input("Voer een positief geheel getal in: "))

# Initialiseer een lege lijst om de delers te bewaren
delers = []

# Ga door elk mogelijk deler van het getal
for i in range(1, getal + 1):
    # Als het getal deelbaar is door i (de rest na deling is 0)
    if getal % i == 0:
        # Voeg i toe aan de lijst van delers
        delers.append(i)

# Print de delers
print(f"De delers van {getal} zijn:")
print(delers)
