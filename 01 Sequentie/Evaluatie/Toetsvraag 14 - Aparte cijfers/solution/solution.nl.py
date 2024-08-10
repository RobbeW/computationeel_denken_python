# Een getal vragen
getal = int( input( 'Geef een getal in kleiner dan 10 000: ' ) )

# Berekeningen
D = ( getal// 1000 ) % 10
H = ( getal // 100 ) % 10
T = ( getal // 10 ) % 10
E = getal % 10

# Uitvoer
print( "Duizendtallen =", D )
print( "Honderdtallen =", H )
print( "Tientallen =", T )
print( "Eenheden =", E )
