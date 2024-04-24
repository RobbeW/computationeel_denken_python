import math
# Invoer vragen
z = float( input( "Geef de zijde in: " ) )
n = int( input( "Geef het volgnummer in: " ) )

# Berekeningen + uitvoer
print("Het eerste vierkant heeft als oppervlakte", round(z**2, 4), "cm².")
aantal = 1
for i in range(n):
    aantal = aantal + 2**(i+1)
    z = z/math.sqrt(2)
    A = z**2
    print("In iteratie", i+1, "zijn er", aantal, "vierkanten in het totaal en is de oppervlakte van het kleinste vierkant",round(A, 4),"cm².")
