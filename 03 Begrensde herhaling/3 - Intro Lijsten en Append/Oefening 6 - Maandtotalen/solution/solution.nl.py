# Laat deze code staan
invoer = input("Geef een lijst in, gescheiden door spaties: ")
kaart1 = list(map(int, invoer.split()))
invoer = input("Geef een lijst in, gescheiden door spaties: ")
kaart2 = list(map(int, invoer.split()))

# Schrijf hieronder je programmma
totalen = []
if len(kaart1) < len(kaart2): # eerste kaart is voor de eerste 6 maanden
    for i in range(len(kaart1)):
        totalen.append( kaart1[i] + kaart2[i])
    for i in range(6, len(kaart2)):
        totalen.append( kaart2[i])
else:                         # tweede kaart is voor de eerste 6 maanden
    for i in range(len(kaart2)):
        totalen.append( kaart2[i] + kaart1[i])
    for i in range(6, len(kaart1)):
        totalen.append( kaart1[i])

print(totalen)
