getal = int( input( "Geef een getal in: " ) )

priem = True
for i in range(2,getal):
    if getal % i == 0:
        priem = False

if not priem:
    print(getal, "is een samengesteld getal.")
else:
    print(getal, "is niet samengesteld.")
