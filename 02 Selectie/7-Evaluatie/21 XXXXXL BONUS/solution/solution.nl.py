# Basisprijs per verpakking vaatwastabletten:
prijs_per_verpakking = 5.99

# Invoer:
aantal = int(input("Geef het aantal verpakkingen in: "))
code = input("Geef de kortingscode in (hamster20, hamster30 of GEEN): ")

# XXL BONUS: 2+5 gratis, 7 halen = 2 betalen:
groepen_van_zeven = aantal // 7
rest = aantal % 7

# Aantal te betalen verpakkingen na XXL BONUS-actie:
te_betalen_verpakkingen = groepen_van_zeven * 2 + rest

# Totaalbedrag na XXL BONUS-actie (voor extra korting):
totaal = te_betalen_verpakkingen * prijs_per_verpakking

# Extra korting in procent bepalen:
if (code == "hamster30" or code == "HAMSTER30") and aantal >= 7:
    korting_procent = 0.30
elif (code == "hamster20" or code == "HAMSTER20") and aantal >= 2:
    korting_procent = 0.20


# Eindprijs berekenen met extra korting:
eindprijs = totaal * (1 - korting_procent)
eindprijs = round(eindprijs, 2)

# Uitvoer: 
print("Aantal verpakkingen:", aantal)
print("Te betalen verpakkingen na XXL BONUS-actie:", te_betalen_verpakkingen)
print("De extra korting bedraagt", korting_procent, "%.")
print("De eindprijs is", eindprijs, "euro.")
