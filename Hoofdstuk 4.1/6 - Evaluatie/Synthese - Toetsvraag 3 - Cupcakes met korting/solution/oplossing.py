# prijs per cupcake
prijs_cupcake = 1.2

# vraag de gebruiker naar het aantal te bestellen cupcakes
aantal_cupcakes = int(input("Hoeveel cupcakes wilt u? "))

# bereken de totaalprijs zonder korting
totaalprijs_zonder_korting = prijs_cupcake * aantal_cupcakes

# bepaal de korting en bereken de totaalprijs met korting
if aantal_cupcakes < 10:
    totaalprijs = totaalprijs_zonder_korting
elif 10 <= aantal_cupcakes < 50:
    totaalprijs = totaalprijs_zonder_korting * 0.9
elif 50 <= aantal_cupcakes < 100:
    totaalprijs = totaalprijs_zonder_korting * 0.85
else:
    totaalprijs = totaalprijs_zonder_korting * 0.75

# druk de totaalprijs na korting af op het scherm
print("De totaalprijs van de cupcakes na toepassing van de korting bedraagt", round(totaalprijs,2), "euro.")
