import math

# Zijde vragen
a = float( input( 'Geef de zijde in (in cm): ' ) )

# Oppervlakte berekenen
R = a / 10 * math.sqrt( 50 + 10 * math.sqrt( 5 ) )
r = a / 10 * math.sqrt( 25 + 10 * math.sqrt( 5 ) )

A = math.pi * R**2 - math.pi * r**2

# Weergeven op het scherm
print()
print( "De oppervlakte bedraagt", round(A, 2), "cm².")
