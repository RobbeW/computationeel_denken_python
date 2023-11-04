import math

# Grondtal vragen aan de gebruiker
a = int( input( 'Geef de natuurlijk getal in:' ) )

# Schatting bepalen
b = math.floor( math.sqrt( a ) )
c = a / b

schatting = round( ( b + c ) / 2, 1 )

# Echte waarde bepalen
echt = round( math.sqrt( a ), 3 )

# Weergeven op het scherm
print( "De vierkantswortel van", a, "wordt geschat als", schatting, "en is in werkelijkheid", echt )
