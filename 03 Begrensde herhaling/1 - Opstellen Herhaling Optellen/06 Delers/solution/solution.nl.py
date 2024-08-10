# Vraag een getal
getal = int( input( "Geef de getal in: " ) )

# Controleer delers
for d in range(1, getal+1):
    if getal % d == 0:
        print(d, "is een deler van", getal)
