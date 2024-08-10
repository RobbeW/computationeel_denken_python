# Vraag een getal
getal = int( input( "Geef de getal in: " ) )

# Controleer delers
aantal = 0
for d in range(1, getal+1):
    if getal % d == 0:
        aantal += 1

if aantal % 2 != 0:
    print(getal,"is een volkomen kwadraat.")
else:
    print(getal,"is geen volkomen kwadraat.")
