import math
# Vraag de gebruiker naar het aantal minuten
minuten = int(input("Geef het aantal minuten dat je fietste in: "))

# Aantal blokken
aantal = math.ceil(minuten / 20)

# Kostprijs bepalen
if minuten < 4:
    kost = 0.29
elif aantal <= 3:
    kost = aantal * 0.45
elif aantal <= 6:
    kost = 3 * 0.45 + (aantal - 3) * 0.65
elif aantal <= 9:
    kost = 3 * 0.45 + 3 * 0.65 + (aantal - 6) * 0.80
else:
    kost = 3 * 0.45 + 3 * 0.65 + 3 * 0.80 + (aantal - 9) * 1.00

# Uitvoer
print(f"Kostprijs: € {round(kost, 2)}")
