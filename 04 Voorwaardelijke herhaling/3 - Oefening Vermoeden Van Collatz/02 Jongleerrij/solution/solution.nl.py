import math
getal = int(input('Voer een geheel getal in: '))

print(getal)
while getal != 1: 
    if getal % 2 == 0:
        getal = math.floor(math.sqrt(getal))
    else:
        getal = math.floor(math.sqrt(getal**3))
    print(getal)