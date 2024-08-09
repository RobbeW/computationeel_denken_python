import math

# Vraag de gebruiker naar de lengtes van de zijden
zijde_a = float(input("Geef de lengte van zijde [a] in: "))
zijde_b = float(input("Geef de lengte van zijde [b] in: "))

# Gebruik de stelling van Pythagoras om de lengte van de schuine zijde te berekenen
zijde_c = math.sqrt(zijde_a ** 2 + zijde_b ** 2)

# Rond de berekende lengte af tot twee decimalen
zijde_c_afgerond = round(zijde_c, 2)

# Print het resultaat
print("De lengte van de schuine zijde [c] is", zijde_c_afgerond, "cm.")
