getal = int( input( "Geef een getal in: " ) )

aantal = 0
for i in range(2, getal):
    if getal % i == 0:
        aantal += 1
        if (getal // i) % i == 0:
            aantal += 1

if aantal == 2:
    print(getal, "is semipriem.")
else:
    print(getal, "is niet semipriem.")
