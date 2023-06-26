# Vraag de gebruiker naar een geheel getal
getal = int(input("Voer een geheel getal in: "))

# Bepaal het kwadraat van het getal
kwadraat = getal ** 2

# Bepaal de restwaarde van het kwadraat gedeeld door 2
restwaarde = kwadraat % 2

# Print de resultaten
print("Het kwadraat van het getal is:", kwadraat)
print("De restwaarde van", kwadraat, "/ 2 =", restwaarde)

