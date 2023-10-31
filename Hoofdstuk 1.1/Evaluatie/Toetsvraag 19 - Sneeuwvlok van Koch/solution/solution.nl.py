import math

# Zijde vragen
z = float( input( 'Geef de zijde in (in cm): ' ) )

# Oppervlakte berekenen
A = 2 * z**2 * math.sqrt(3) / 5

# Weergeven op het scherm
print( "De oppervlate is", round(A, 2), "cm².")
