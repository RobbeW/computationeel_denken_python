# Vraag de gebruiker om het aantal normale en large pizza's
aantal_normaal = int(input("Voer het aantal normale pizza's in: "))
aantal_large = int(input("Voer het aantal large pizza's in: "))

# Bereken het totale aankoopbedrag
totale_aankoop = aantal_normaal * 12.80 + aantal_large * 16.80

# Bepaal de toegepaste korting op basis van het aankoopbedrag
if totale_aankoop > 55:
    korting = 0.3
elif totale_aankoop > 40:
    korting = 0.2
elif totale_aankoop > 30:
    korting = 0.12
elif totale_aankoop > 25:
    korting = 0.8
else:
    korting = 0

# Bereken de te betalen prijs na korting
prijs_na_korting = round(totale_aankoop * (1 - korting), 2)

# Print de te betalen prijs op het scherm
print("De te betalen prijs na korting is", prijs_na_korting, "euro.")
