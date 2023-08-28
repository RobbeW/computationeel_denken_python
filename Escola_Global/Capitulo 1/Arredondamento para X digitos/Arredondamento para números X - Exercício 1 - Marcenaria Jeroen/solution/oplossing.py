# Vraag de gebruiker naar de lengte en breedte
lengte = float(input("Voer de lengte in: "))
breedte = float(input("Voer de breedte in: "))

# Bereken de omtrek en oppervlakte
omtrek = round(2*(lengte + breedte),2)
oppervlakte = round(lengte * breedte, 2)

# Print de resultaten met 2 decimalen
print("De omtrek bedraagt:", omtrek, "centimeter.")
print("De oppervlakte bedraagt:", oppervlakte, "vierkante centimeter.")
