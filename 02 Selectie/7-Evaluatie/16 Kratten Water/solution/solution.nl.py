# Vraag het aantal flessen
aantal = int(input("Geef het aantal flessen in: "))

# Aantal kratten van 12 berekenen
kratten12 = aantal // 12
rest = aantal % 12

# Aantal kratten van 6 berekenen
kratten6 = rest // 6
rest = rest % 6

# Aantal kratten van 4 berekenen
kratten4 = rest // 4
overschot = rest % 4

# Uitvoer:
print("kratten 12:", kratten12)
print("kratten 6:", kratten6)
print("kratten 4:", kratten4)
print("overschot flessen:", overschot)
