import math

# De oppervlakte van het grootste vierkant
oppervlakte = float( input( 'Geef de grootste oppervlakte in (in m²): ' ) )

# Bereken de lengte van de zijde van het grootste vierkant
zijde = math.sqrt(oppervlakte)
print("De lengte van de zijde van vierkant 1 is:", round( zijde, 2 ), "m.")

# Bereken de oppervlakte en de lengte van de zijde van elk kleiner vierkant
for i in range(3):
    oppervlakte /= 4
    zijde = math.sqrt( oppervlakte )
    print("De oppervlakte van vierkant", i+2, "is:", round( oppervlakte, 2), "m².")
    print("De lengte van de zijde van vierkant", i+2, "is:", round( zijde, 2), "m.")

