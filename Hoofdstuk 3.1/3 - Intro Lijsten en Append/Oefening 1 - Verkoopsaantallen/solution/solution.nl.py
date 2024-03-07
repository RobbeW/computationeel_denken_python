# Lijst met namen van de vestigingen
vestigingen = ["Brugge", "Gent", "Kortrijk", "Antwerpen", "Brussel"]

# Variabele om de som van de bedragen bij te houden
som = 0

# We itereren over de lijst met namen van vestigingen
for vestiging in vestigingen:
    # Vraag de gebruiker om het verkoopbedrag voor deze vestiging
    bedrag = float(input("Voer het totaal in voor de winkel in " + vestiging + ": "))
    
    # Voeg het bedrag toe aan de som
    som += bedrag

# Print het totale bedrag naar het scherm

print("Het maandtotaal bedraagt", round(som, 2), "euro.")
