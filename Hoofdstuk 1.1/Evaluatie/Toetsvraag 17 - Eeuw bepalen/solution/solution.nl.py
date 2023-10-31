# Invoer vragen aan de gebruiker
jaartal = int( input( 'Geef het jaartal in:' ) )

# Eeuw bepalen
eeuw = jaartal // 100 + 1

# Weergeven op het scherm
print( str(eeuw) + 'e eeuw')
