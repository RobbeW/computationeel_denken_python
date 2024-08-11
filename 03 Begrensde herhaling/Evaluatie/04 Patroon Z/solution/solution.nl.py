# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

# Berekening
for i in range(n):
    if i in (0, n - 1):
        print("X" * n)
    else:
        print(" "*(n-i-1) + "X")
