getal = int( input( "Geef een getal in: " ) )

i = 2
while getal > 1:
    if getal % i == 0:
        print(i, "is een deler.")
        getal = getal // i
    else:
        i +=1
