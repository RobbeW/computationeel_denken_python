import math

# Invoer
h_muur = float( input( 'Voer de hoogte van de muur in meter in: ' ) )
b_muur = float( input( 'Voer de breedte van de muur in meter in: ' ) )

z_tegel = float( input('Voer de breedte van de tegel in cm in: ' ) )
soort = input( 'Voer de soort in: ' )

# Verwerking
aantal_hoogte = math.ceil( h_muur * 100 / z_tegel )
aantal_breedte = math.ceil( b_muur * 100 / z_tegel )

aantal_tegels = math.ceil( aantal_hoogte * aantal_breedte * 1.07 )

# Uitvoer
print( 'U heeft',aantal_tegels, soort, 'tegels nodig voor een muur van', h_muur ,'x', b_muur ,'m.')
