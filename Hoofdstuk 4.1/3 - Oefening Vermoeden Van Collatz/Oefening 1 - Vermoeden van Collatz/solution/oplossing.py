getal = int(input('Voer een geheel getal in: '))
while getal != 1: 
    if getal % 2 == 0:
        getal = getal / 2
    else:
        getal = getal * 3 + 1
    print(getal)
print('Stop!')