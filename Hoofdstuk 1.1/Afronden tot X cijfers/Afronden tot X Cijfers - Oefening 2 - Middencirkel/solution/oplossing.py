# Definieer pi
pi = 3.14

# Vraag de gebruiker naar de straal
straal = float(input("Voer de straal in: "))

# Bereken de omtrek en oppervlakte
omtrek = 2 * pi * straal
oppervlakte = pi * straal ** 2

# Print de resultaten met 2 decimalen
print("De omtrek bedraagt:", round(omtrek, 2), "meter.")
print("De oppervlakte bedraagt:", round(oppervlakte, 2), "vierkante meter.")
