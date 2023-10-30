# Vraag de gebruiker om twee gehele getallen
eerste_getal = int(input("Voer het eerste getal in: "))
tweede_getal = int(input("Voer het tweede getal in: "))

# Controleer of de getallen gelijk zijn
if eerste_getal == tweede_getal:
    print("De getallen zijn gelijk.")
# Als ze niet gelijk zijn, controleer welk getal groter is
elif eerste_getal > tweede_getal:
    print("De getallen zijn ongelijk.")
    print("Het grootste getal is", str(eerste_getal) + ".")
else:
    print("De getallen zijn ongelijk.")
    print("Het grootste getal is", str(tweede_getal) + ".")
