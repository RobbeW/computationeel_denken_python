# Vraag bestemming, lijnnummer en ritnummer op:
bestemming = input("Wat is je bestemming? ")
lijnnummer = input("Geef het lijnnummer in: ")
ritnummer = input("Geef het ritnummer in (4 cijfers): ")

# Ticketcode samenstellen door lijnnummer en ritnummer te concateneren:
ticketcode = lijnnummer + ritnummer

# Uitvoer:
print("De bus naar", bestemming, "heeft lijn", lijnnummer + ".")
print("De ticketcode is:", ticketcode)
