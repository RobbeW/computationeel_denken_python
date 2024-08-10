import math

# Decimale graad vragen
graad = float( input( "Geef een decimale graad in: " ) )

# Omzetten
graden = math.floor( graad )
rest = round( graad - graden, 4 )

minuten = math.floor( rest * 60 )
rest = round( rest *60 - minuten, 4 )

seconden = math.floor( rest * 60 )

# Weergeven op het scherm
print( "Dit komt overeen met", graden, "graden", minuten, "minuten en", seconden, "seconden.")
