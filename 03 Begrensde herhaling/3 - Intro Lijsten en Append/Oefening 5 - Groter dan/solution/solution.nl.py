# Laat deze code staan
invoer = input("Geef een lijst in, gescheiden door spaties: ")
lijst = list(map(int, invoer.split()))

# Vraag nog naar de grenswaarde
grenswaarde = int( input( "Geef een grenswaarde in: " ) )

# Schrijf hieronder je programmma
nieuw = []
for getal in lijst:
    if getal > grenswaarde:
        nieuw.append(getal)

print(nieuw)
