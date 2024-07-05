# prijs per cupcake
prijs_cupcake = 1.2

# vraag de gebruiker naar het aantal te bestellen cupcakes
aantal_cupcakes = int(input("Hoeveel cupcakes wilt u? "))

# bereken de totaalprijs zonder korting
totaalprijs = prijs_cupcake * aantal_cupcakes

# bepaal de korting en bereken de totaalprijs met korting
if 10 <= aantal_cupcakes < 50:
    totaalprijs *= 0.9
elif aantal_cupcakes < 100:
    totaalprijs *= 0.85
elif aantal_cupcakes >= 100:
    totaalprijs *= 0.75

# druk de totaalprijs na korting af op het scherm
print()
print("De totaalprijs van de cupcakes bedraagt", round(totaalprijs, 2), "euro.")
