# Gegevens vragen
n = int( input( 'Geef het getal in: ' ) )

# Berekening
for i in range( n ):
   print(" "*i + "*" + " "*(n-i-1) + "*" + " "*(n-i-1) + "*")

print("*"*(2*n+1))

for i in range( n ):
   print(" "*(n-i-1) + "*" + " "*(i) + "*" + " "*(i) + "*")