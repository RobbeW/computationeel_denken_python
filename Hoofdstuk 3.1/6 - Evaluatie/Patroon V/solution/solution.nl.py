# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

# Berekening
for i in range( n ):
    r1 = i
    r2 = 2 * n - 2 -1 - 2*i
    if i == n-1:
        print(" " * r1 + "*")
    else:
        print(" "*r1 + "*"+" "*r2+"*")
