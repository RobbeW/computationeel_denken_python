# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

print()
# Berekening
for i in range(n):
    if i == 0 or i == n-1:
        print("x" + (n-2)*" "+"x")
    else:
        print("x"+" "*(i-1)+"x"+" "*(n-2-i)+"x")
