# Invoer vragen van de klant
bedrag = float(input("Voer het bedrag in: "))
korting = int(input("Voer de hoeveelheid korting in: "))

# Restbedrag berekenen
rest = bedrag * ( 1 - korting / 100 )

# Weergeven op het scherm
print("Je moet nog €", rest, "betalen.")