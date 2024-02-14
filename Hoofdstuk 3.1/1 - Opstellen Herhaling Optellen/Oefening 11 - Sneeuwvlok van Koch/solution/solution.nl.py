# Invoer vrage
z = float( input( 'Geef de zijde in (in cm): ' ) )
n = int( input( 'Geef de iteratie in: ' ) )

# Oppervlakte berekenen
print()
P = 3 * z
print("De startomtrek was", round(P, 2), "cm.")
for i in range(n):
    P *= 4/3
    print("In iteratie", i+1, "bedraagt de omtrek", round(P, 2), "cm.")
