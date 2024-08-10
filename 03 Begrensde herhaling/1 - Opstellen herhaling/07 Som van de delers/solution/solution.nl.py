# Vraag een getal
getal = int( input( "Geef de getal in: " ) )

som = 0
# Controleer delers
for d in range(1, getal):
    if getal % d == 0:
        som  += d

print("De som van de echte delers is:", som)
if som < getal:
    print("Dit getal is gebrekkig.")
elif som > getal:
    print("Dit getal is overvloedig.")
else:
    print("Dit getal is perfect.")
