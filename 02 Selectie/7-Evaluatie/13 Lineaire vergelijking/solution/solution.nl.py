a = int(input("Geef de waarde van a in: "))
b = int(input("Geef de waarde van b in: "))

if a == 0 and b == 0:
    print("Dit is een onbepaalde vergelijking.")
elif a == 0:
    print("Ledige oplossingenverzameling, deze vergelijking is vals.")
else:
    c = round(-b / a, 1)
    print("Oplossingenverzameling = {", c, "}")
