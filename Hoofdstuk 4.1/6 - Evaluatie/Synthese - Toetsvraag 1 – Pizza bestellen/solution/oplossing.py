# prijzen van de extra's
prijs_gehaktballetjes = 1
prijs_pepertjes = 0.5
prijs_olijfjes = 0.3

# prijs van de pizza zonder extra's
prijs_pizza = 9

# vraag de gebruiker hoeveel van elke extra hij/zij/hun wenst
aantal_gehaktballetjes = int(input("Hoeveel gehaktballetjes wenst u? "))
aantal_pepertjes = int(input("Hoeveel pepertjes wenst u? "))
aantal_olijfjes = int(input("Hoeveel olijfjes wenst u? "))

# bereken de totaalprijs
totaalprijs = prijs_pizza + prijs_gehaktballetjes * aantal_gehaktballetjes + prijs_pepertjes * aantal_pepertjes + prijs_olijfjes * aantal_olijfjes

# druk de totaalprijs af
print("De totaalprijs van de pizza bedraagt", totaalprijs, "euro.")
