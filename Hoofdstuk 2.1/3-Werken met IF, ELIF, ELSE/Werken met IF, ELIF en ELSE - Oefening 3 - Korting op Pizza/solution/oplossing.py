# Vraag de gebruiker om het aantal normale en large pizza's
aantal_normaal = int(input("Voer het aantal normale pizza's in: "))
aantal_large = int(input("Voer het aantal large pizza's in: "))

# Bereken het totale aankoopbedrag
totale_aankoop = aantal_normaal * 12.80 + aantal_large * 16.80

# Bepaal de toegepaste korting op basis van het aankoopbedrag
if totale_aankoop > 55:
    korting = 30
elif totale_aankoop > 40:
    korting = 20
elif totale_aankoop > 30:
    korting = 12
elif totale_aankoop > 25:
    korting = 8
else:
    korting = 0

# Bereken de te betalen prijs na korting
prijs_na_korting = totale_aankoop * (1 - korting / 100)

# Print de te betalen prijs op het scherm
print(f"De te betalen prijs na korting is {prijs_na_korting:.2f} euro.")
