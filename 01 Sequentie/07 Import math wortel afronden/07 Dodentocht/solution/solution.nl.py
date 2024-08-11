# Invoer
afstand = float(input("Geef de afstand in: "))
snelheid = float(input("Geef de gemiddelde snelheid in in: "))

# Tijd die verlopen is
tijd = afstand / snelheid

# Hoeveel blijft er nog af te leggen?
afstand_resterend = 100 - afstand
tijd_resterend = 24 - tijd

# Aan welke snelheid dus?
snelheid = round(afstand_resterend / tijd_resterend, 1)

# Uitvoer
print("Je moet minstens", snelheid, "km/u blijven wandelen.")
