# Vraag de gebruiker om het bestelde bedrag en de kortingscode
bestelde_bedrag = float(input("Voer het bestelde bedrag in: "))
kortingscode = input("Voer de kortingscode in (indien van toepassing): ")

# Bereken de korting op basis van de ingevoerde kortingscode
if kortingscode == "november10":
    korting = 0.10
elif kortingscode == "Twitch20":
    korting = 0.20
else:
    korting = 0

# Pas de korting toe en voeg de leveringskosten toe
te_betalen_bedrag = bestelde_bedrag * (1 - korting) + 4.80

# Print het te betalen bedrag op het scherm
print(f"Het te betalen bedrag is", te_betalen_bedrag, "euro.")
