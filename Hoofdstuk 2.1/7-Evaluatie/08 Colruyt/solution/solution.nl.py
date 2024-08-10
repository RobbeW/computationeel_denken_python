# Vraag het aantal
aantal = int(input("Geef het aantal verpakkingen in:"))

# Kostprijs
bedrag = aantal * 3.29
if  aantal == 2:
    bedrag *= 0.8
elif aantal > 2 :
    bedrag *= 0.7

# Weergave
print("De kostprijs is", round(bedrag, 2), "euro.")
