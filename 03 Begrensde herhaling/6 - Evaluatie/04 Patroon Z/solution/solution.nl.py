# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

# Berekening
for i in range( n):
    if i == 0 or i == n-1:
        print("*" * n)
    else:
        print(" "*(n-i-1) + "*")
