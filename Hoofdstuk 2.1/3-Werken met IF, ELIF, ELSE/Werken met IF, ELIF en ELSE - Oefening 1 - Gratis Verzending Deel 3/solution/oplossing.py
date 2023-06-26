# Vraag de gebruiker om het bestelde bedrag
bestelde_bedrag = float(input("Voer het aankoopbedrag in: "))

# Bepaal of de gebruiker 10% korting krijgt
if bestelde_bedrag >= 100:
    bestelde_bedrag *= 0.9
    print("Je krijgt 10% korting.")
    print("Je krijgt gratis verzending.")

# Bepaal of de gebruiker gratis verzending krijgt
if bestelde_bedrag < 20:
    bestelde_bedrag += 4
    print("Je krijgt geen gratis verzending.")
else:
    print("Je krijgt gratis verzending.")
    
# Druk het totaalbedrag af in een volzin
print(f"Het totaalbedrag is {round(bestelde_bedrag, 2)} euro.")
