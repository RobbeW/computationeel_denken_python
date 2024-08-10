# Lees de zijden in
a = int( input( "Geef de eerste zijde in: ") )
b = int( input( "Geef de tweede zijde in: ") )
c = int( input( "Geef de derde zijde in: ") )

# Welke soort driehoek is het?
if( a == b or a == c or b == c):
    if (a == b and b == c):
        print ( 'Deze driehoek is gelijkzijdig.' )
    else:
        print( 'Deze driehoek is gelijkbenig.' )
else:
    print( 'Deze driehoek is willekeurig.' )
