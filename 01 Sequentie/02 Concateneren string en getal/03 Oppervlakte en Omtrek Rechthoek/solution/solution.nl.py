# Vraag de gebruiker naar de lengte en breedte van de rechthoek
lengte = float(input("Voer de lengte van de rechthoek in: "))
breedte = float(input("Voer de breedte van de rechthoek in: "))

# Bereken de oppervlakte en omtrek van de rechthoek
oppervlakte = lengte * breedte
omtrek = 2 * (lengte + breedte)

# Print de oppervlakte en omtrek van de rechthoek
print("De oppervlakte van de rechthoek is", oppervlakte, "m².")
print("De omtrek van de rechthoek is", omtrek, "m.")
