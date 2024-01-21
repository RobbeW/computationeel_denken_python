# Vraag de gebruiker om het bestelde bedrag en de kortingscode
bestelde_bedrag = float(input("Voer het bestelde bedrag in: "))
kortingscode = input("Voer de kortingscode in (indien van toepassing): ")

# Bereken de korting op basis van de ingevoerde kortingscode
if kortingscode == "november10":
    bestelde_bedrag *= ( 1 - 0.10 )
elif kortingscode == "Twitch20":
    bestelde_bedrag *= ( 1 - 0.20)

# Pas de korting toe en voeg de leveringskosten toe
te_betalen_bedrag = round( bestelde_bedrag + 4.80, 2 )

# Print het te betalen bedrag op het scherm
print("Het te betalen bedrag is", te_betalen_bedrag, "euro.")
