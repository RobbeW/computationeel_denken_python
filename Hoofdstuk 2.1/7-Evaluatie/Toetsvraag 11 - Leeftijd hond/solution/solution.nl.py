# Vraag het aantal
aantal = int(input("Geef het aantal hondenjaren in:"))

# Leeftijd berekenen
if  aantal == 1:
    leeftijd = 15
elif aantal == 2:
    leeftijd = 24
else:
    leeftijd = 24 + ( aantal - 2 ) * 5

# Weergave
print("Deze hond is ongeveer", leeftijd, "mensenjaren oud.")
