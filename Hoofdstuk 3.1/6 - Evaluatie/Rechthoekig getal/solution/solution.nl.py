getal = int( input( "Geef een getal in: " ) )

rechthoekig = False
for i in range(1,getal):
    if getal % i == 0 and getal % (i+1) == 0 and i*(i+1) == getal:
        rechthoekig = True

print()
if rechthoekig:
    print(getal, "is een rechthoekig getal.")
else:
    print(getal, "is niet rechthoekig.")
