# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

# Tekenen
for i in range( 2*n -1 ):
    spaces = max( 2*n-2-2*i, 2*(i-n)+2 )
    stars = min( 2*i, 2*n-4-2*(i-n) )
    
    print(" "*spaces+ "* "*stars + "*")
