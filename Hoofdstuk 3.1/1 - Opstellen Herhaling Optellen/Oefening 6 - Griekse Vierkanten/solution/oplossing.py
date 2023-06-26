import math

# De oppervlakte van het grootste vierkant
oppervlakte_1 = 144

# Bereken de lengte van de zijde van het grootste vierkant
zijde_1 = math.sqrt(oppervlakte_1)
print("De lengte van de zijde van vierkant 1 is:", zijde_1, "meter")

# Bereken de oppervlakte en de lengte van de zijde van elk kleiner vierkant
for i in range(2, 5):
    oppervlakte_i = oppervlakte_1 / 4
    zijde_i = math.sqrt(oppervlakte_i)
    print("De lengte van de zijde van vierkant", i, "is:", zijde_i, "meter")
    print("De oppervlakte van vierkant", i, "is:", oppervlakte_i, "vierkante meter")
    
    
    # Het volgende vierkant wordt het kleinere vierkant
    oppervlakte_1 = oppervlakte_i
