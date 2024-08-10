import math

# Vraag de gebruiker om input voor zwembad Eddy
diameter_eddy = float(input("Geef de diameter in van het zwembad van Eddy: "))
diepte_eddy = float(input("Geef de diepte in van het zwembad van Eddy: "))

# Vraag de gebruiker om input voor zwembad Freddy
diameter_freddy  = float(input("Geef de diameter in van het zwembad van Freddy: "))
diepte_freddy = float(input("Geef de diepte in van het zwembad van Freddy: "))

# Bereken het volume voor beide zwembaden
# Volume = pi * r^2 * h
volume_eddy = math.pi * (diameter_eddy / 2) ** 2 * diepte_eddy
volume_freddy = math.pi * (diameter_freddy / 2) ** 2 * diepte_freddy

# Bepaal wie het grootste zwembad heeft
if volume_eddy > volume_freddy:
    print("Eddy heeft het grootste zwembad van de buurt.")
    print("Het zwembad heeft een volume van", round(volume_eddy, 2), "m³.")
elif volume_eddy < volume_freddy:
    print("Freddy heeft het grootste zwembad van de buurt.")
    print("Het zwembad heeft een volume van", round(volume_freddy, 2), "m³.")
else:
    print("Eddy en Freddy hebben even grote zwembaden.")
    print("Beide zwembaden hebben een volume van", round(volume_eddy, 2), "m³.")
