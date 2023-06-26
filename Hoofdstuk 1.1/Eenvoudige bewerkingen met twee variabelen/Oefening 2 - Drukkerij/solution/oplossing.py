# Vaste kost voor het drukken van het tijdschrift
vaste_kost = 2000

# Kost per exemplaar
kost_per_exemplaar = 5

# Vraag de gebruiker om het aantal exemplaren dat gedrukt moet worden
aantal_exemplaren = int(input("Hoeveel exemplaren moeten gedrukt worden? "))

# Bereken de totale kostprijs
totale_kostprijs = vaste_kost + (aantal_exemplaren * kost_per_exemplaar)

# Bereken de prijs per exemplaar
prijs_per_exemplaar = totale_kostprijs / aantal_exemplaren

# Print de totale kostprijs en de prijs per exemplaar naar het scherm
print(totale_kostprijs)
print(prijs_per_exemplaar)
