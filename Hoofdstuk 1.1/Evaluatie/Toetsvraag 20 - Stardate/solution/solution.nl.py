import math

# Invoer vragen aan de gebruiker
stardate = float( input( 'Geef de stardate in: ' ) )

# Eeuw bepalen
Y = int( stardate // 100 + 1900 )
M = math.floor(stardate) % 100
D = int( ( stardate * 100 ) % 100 )

# Weergeven op het scherm
print( "Dit komt overeen met", str(D)+"-"+str(M)+"-"+str(Y)+"." )
