# prijs per cupcake
prijs_cupcake = 1.2

# vraag de gebruiker naar het aantal te bestellen cupcakes
aantal_cupcakes = int(input("Hoeveel cupcakes wilt u? "))

# bereken de totaalprijs
totaalprijs = prijs_cupcake * aantal_cupcakes

# druk de totaalprijs af op het scherm
print("De totaalprijs van de cupcakes bedraagt", round(totaalprijs, 2), "euro.")
