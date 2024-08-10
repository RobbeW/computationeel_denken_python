import math

# Invoer vragen
z = float( input( 'Geef de zijde in (in cm): ' ) )
n = int( input( 'Geef de iteratie in: ' ) )

# Lengte berekenen
aantal = 2
print("De startlengte was", round(aantal * z, 2), "cm.")
for i in range(n):
    z /= math.sqrt(2)
    aantal *= 2
    print("In iteratie", i+1, "bedraagt de lengte van de draakkromme", round(aantal * z, 2), "cm.")
