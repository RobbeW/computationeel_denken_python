import math

# Gegevens van het prisma vragen
d = float( input( "Geef de lengte van de kleine diagonaal (in cm): " ) )
D = float( input( "Geef de lengte van de grote diagonaal (in cm): " ) )
h = float( input( "Geef de lengte van de hoogte (in cm): " ) )

# Berekeningen
V = ( d * D / 2 ) * h
b = math.sqrt( (d/2)**2 + (D/2)**2)
A = d * D + 4 * h * b

# Uitvoer
print( "Het prisma heeft een volume van", round(V, 2), "cm³." )
print( "Het prisma heeft een oppervlakte van", round(A, 3), "cm²." )
