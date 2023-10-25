import math

# Invoer vragen aan de gebruiker
r = float( input( 'Geef de straal in:' ) )
h = float( input( 'Geef de hoogte in:' ) )

# Berekeningen
A = 2 * math.pi * r * h + 2 * math.pi * r**2
V = math.pi * r**2 * h

# Uitvoer verzorgen
print("Oppervlakte:", round(A, 3), "cm²." )
print("Volume:", round(V, 3), "cm³." )
