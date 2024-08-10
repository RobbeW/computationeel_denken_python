# Lees de zijden in
a = int( input( "Geef de eerste zijde in: ") )
b = int( input( "Geef de tweede zijde in: ") )
c = int( input( "Geef de derde zijde in: ") )

## onderzoek
if( a + b > c and b + c > a and a + c > b):
    print( 'Deze zijden vormen een driehoek.' )
else:
    print( 'Deze zijden vormen geen driehoek.' )
