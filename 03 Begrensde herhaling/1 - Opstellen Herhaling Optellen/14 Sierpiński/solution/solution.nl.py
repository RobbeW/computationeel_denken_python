import math

# Invoer vragen
A = float( input( 'Geef de oppervlakte in (in cm²): ' ) )
n = int( input( 'Geef de iteratie in: ' ) )

# Berekeningen berekenen
aantal = 1
print( "De startoppervlakte was", round(A, 2), "cm²." )
for i in range( n ):
    aantal *= 3
    A *= 3 / 4
    print("Na iteratie", i+1, "zijn er", aantal, "driehoeken en resteert er", round(A, 2), "cm².")
