# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

# Berekening
for i in range( n ):
   print(" "*i + "X" + " "*(n-i-1) + "X" + " "*(n-i-1) + "X")

print("X"*(2*n+1))

for i in range( n ):
   print(" "*(n-i-1) + "X" + " "*(i) + "X" + " "*(i) + "X")
