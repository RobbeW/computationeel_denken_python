import math

# Invoer:
x = float(input("Geef de concentratie x in (mg/L): "))

# Teller en noemer apart berekenen:
teller = 7 * math.sqrt(x) + math.pi - (8 - x ** 3)
noemer = (math.pi ** 2) + 45.3 * x - math.sqrt(89.1)

# R berekenen en afronden:
R = math.sqrt(teller / noemer)
R = round(R, 4)

# Onder- en bovengrens bepalen:
ondergrens = math.floor(R)
bovengrens = ondergrens + 1

# Uitvoer: 
print(ondergrens, "<", R, "<", bovengrens)

