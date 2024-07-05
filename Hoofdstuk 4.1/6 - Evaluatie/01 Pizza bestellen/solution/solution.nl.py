# prijs van de pizza zonder extra's
prijs = 13.75

# vraag de gebruiker hoeveel van elke extra hij/zij/hun wenst
vraag = input("Wilt u een cheesy crust pizza? (ja/nee) ")

aantal_groenten = int(input("Hoeveel extra groenten wenst u? "))
aantal_vleessoorten = int(input("Hoeveel extra vleessoorten wenst u? "))

# bereken de totaalprijs
if vraag == "ja":
    prijs += 2

prijs += aantal_groenten * 1.25 + aantal_vleessoorten * 1.50

# druk de totaalprijs af
print("De totaalprijs van de pizza bedraagt", round(prijs, 2), "euro.")
