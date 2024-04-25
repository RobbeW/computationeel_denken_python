getal = int( input( "Geef een getal in: " ) )

rechthoekig = False
for i in range(1,getal):
    if i*(i+1) == getal:
        rechthoekig = True

if rechthoekig:
    print(getal, "is een rechthoekig getal.")
else:
    print(getal, "is niet rechthoekig.")
