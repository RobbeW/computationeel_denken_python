import math

# Vraag de gebruiker naar de lengtes van de rechthoekszijden
rechthoekszijde_1 = int(input("Voer de lengte van rechthoekszijde_1 in (in cm): "))
rechthoekszijde_2 = int(input("Voer de lengte van rechthoekszijde_2 in (in cm): "))

# Bereken de lengte van de schuine zijde met de stelling van Pythagoras
schuine_zijde = math.sqrt(rechthoekszijde_1**2 + rechthoekszijde_2**2)

# Bereken de omtrek van de driehoek
omtrek = rechthoekszijde_1 + rechthoekszijde_2 + schuine_zijde

# Bereken de oppervlakte van de driehoek
oppervlakte = 0.5 * rechthoekszijde_1 * rechthoekszijde_2

# Rond de resultaten af naar twee decimalen
omtrek = round(omtrek, 2)
oppervlakte = round(oppervlakte, 2)

# Print de omtrek en oppervlakte van de driehoek op het scherm
print("De omtrek van de driehoek is", omtrek, "centimeter.")
print("De oppervlakte van de driehoek is", oppervlakte, "vierkante centimeter.")
