import math
# Invoer
r = float( input( 'Geef de straal in (in cm): ' ) )

# Verwerking
h = r * ( math.sqrt(2) / 2 - 3 * math.sqrt(3)/8)

# Weergave
print( 'Het hoogteverschil is', round( h, 2), 'cm.' )
