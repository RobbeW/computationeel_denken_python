import math

# Basisprijs
basisprijs = 2.00

# Vraag de gebruiker naar de massa van het pakje en de afstand
massa_pakje = float(input("Voer de massa van het pakje in (in gram): "))
afstand = float(input("Voer de afstand in (in km): "))

# Bereken het aantal extra kosten voor de massa en de afstand
extra_kosten_massa = math.ceil(massa_pakje / 20) * 0.40
extra_kosten_afstand = math.ceil(afstand / 10) * 0.30

# Bereken de totale prijs
totaalprijs = basisprijs + extra_kosten_massa + extra_kosten_afstand

# Rond de totaalprijs af naar één decimaal
totaalprijs = round(totaalprijs, 1)

# Print de totaalprijs op het scherm
print("De prijs om het pakje te versturen is", totaalprijs, "euro.")
