# Lijst van vierkantnamen
vierkantnamen = ["ABCD", "EFGH", "IJKL", "MNOP", "QRST"]

# Startwaarde van de lengte van de zijde
lengte_zijde = 5

# Itereer over de vierkantnamen
for vierkantnaam in vierkantnamen:
    # Bereken de oppervlakte
    oppervlakte = lengte_zijde ** 2

    # Print de lengte van de zijde en de oppervlakte
    print("De lengte van de zijde van vierkant", vierkantnaam, "is", round(lengte_zijde, 2), "meter en de oppervlakte is", round(oppervlakte, 2), "vierkante meter.")

    # Update de lengte van de zijde voor de volgende iteratie
    lengte_zijde = (2 * oppervlakte) ** 0.5
