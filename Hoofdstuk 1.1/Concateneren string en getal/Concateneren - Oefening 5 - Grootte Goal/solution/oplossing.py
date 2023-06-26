# Vraag de gebruiker naar de lengte en hoogte van de goal
lengte = float(input("Voer de lengte van de goal in: "))
hoogte = float(input("Voer de hoogte van de goal in: "))

# Bereken de omtrek en oppervlakte van de goal
omtrek = 2 * (lengte + hoogte)
oppervlakte = lengte * hoogte

# Print de omtrek en oppervlakte van de goal
print("De omtrek van het kader is", omtrek, "meter.")
print("De oppervlakte van het kader is", oppervlakte, "vierkante meter.")
