# Definieer PI (constnate)
PI = 3.1415

# Vraag de gebruiker naar de straal
straal = float(input("Voer de straal in: "))

# Bereken de omtrek en oppervlakte
omtrek = 2 * PI * straal
oppervlakte = PI * straal ** 2

# Print de resultaten met 2 decimalen
print("De omtrek bedraagt:", round(omtrek, 2), "m.")
print("De oppervlakte bedraagt:", round(oppervlakte, 2), "m².")
