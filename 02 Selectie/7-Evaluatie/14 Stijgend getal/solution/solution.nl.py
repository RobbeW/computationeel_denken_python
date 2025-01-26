getal = int(input("Geef een getal in: "))

H = getal // 100
T = (getal % 100) // 10
E = getal % 10

if H < T and T < E:
    print("Dit getal is strikt stijgend.")
else:
    print("Dit getal is NIET strikt stijgend.")
