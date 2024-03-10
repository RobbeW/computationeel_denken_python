# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

# Berekening
print()
for i in range(n):
    if i == 0 or i == n-1:
        print("*" + (n-2)*" "+"*")
    else:
        print("*"+" "*(i-1)+"*"+" "*(n-2-i)+"*")
