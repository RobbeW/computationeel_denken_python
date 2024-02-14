# Invoer vrage
z = float( input( 'Geef de zijde in (in cm): ' ) )
n = int( input( 'Geef de iteratie in: ' ) )

# Oppervlakte berekenen
print("De startomtrek was", round(3 * z, 2), "cm.")
for i in range(n):
    P = round(3 * z * (4/3)**(i+1), 2)
    print("In iteratie", i+1, "bedraagt de omtrek", P, "cm.")
