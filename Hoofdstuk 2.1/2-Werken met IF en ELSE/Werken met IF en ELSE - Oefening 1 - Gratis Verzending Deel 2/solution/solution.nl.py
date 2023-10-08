# Vraag de gebruiker naar het aankoopbedrag
aankoopbedrag = float(input("Voer het aankoopbedrag in: "))
print()

# Bepaal of de gebruiker in aanmerking komt voor gratis verzending
if aankoopbedrag >= 20:
    print("Je komt in aanmerking voor gratis verzending. Het totaalbedrag is", aankoopbedrag," euro.")
else:
    totaalbedrag = aankoopbedrag + 4
    print("Je komt niet in aanmerking voor gratis verzending. Het totaalbedrag inclusief verzending is", totaalbedrag, "euro.")
