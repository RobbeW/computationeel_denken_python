import math

# Vraag de gebruiker naar de lengtes van de diagonalen
grote_d = int(input("Voer de lengte van de grote diagonaal in (in cm): "))
kleine_d = int(input("Voer de lengte van de kleine diagonaal in (in cm): "))

# Bereken de lengte van de schuine zijde met de stelling van Pythagoras
halve_grote_d = grote_d / 2
halve_kleine_d = kleine_d / 2

schuine_zijde = math.sqrt(halve_grote_d**2 + halve_kleine_d**2)

# Bereken de omtrek van de ruit
omtrek = schuine_zijde * 4

# Bereken de oppervlakte van de ruit
oppervlakte = grote_d * kleine_d / 2

# Rond de resultaten af naar twee decimalen
omtrek = round(omtrek, 2)
oppervlakte = round(oppervlakte, 2)

# Print de omtrek en oppervlakte van de ruit op het scherm
print("De omtrek van de ruit is", omtrek, "cm.")
print("De oppervlakte van de ruit is", oppervlakte, "cm².")
