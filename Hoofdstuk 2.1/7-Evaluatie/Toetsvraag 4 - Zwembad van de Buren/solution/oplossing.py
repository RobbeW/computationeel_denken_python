import math

# Vraag de gebruiker om input voor zwembad Eddy
diepte_eddy = float(input("Geef de diepte in van het zwembad van Eddy: "))
diameter_eddy = float(input("Geef de diameter in van het zwembad van Eddy: "))


# Vraag de gebruiker om input voor zwembad Thierry
diepte_thierry = float(input("Geef de diepte in van het zwembad van Thierry: "))
diameter_thierry = float(input("Geef de diameter in van het zwembad van Thierry: "))


# Bereken het volume voor beide zwembaden
# Volume = Pi * r^2 * h
volume_eddy = math.pi * (diameter_eddy / 2) ** 2 * diepte_eddy
volume_thierry = math.pi * (diameter_thierry / 2) ** 2 * diepte_thierry

# Bepaal wie het grootste zwembad heeft
if volume_eddy > volume_thierry:
    print("Eddy heeft het grootste zwembad van de buurt.")
    print("Het zwembad heeft een volume van ", round(volume_eddy, 2), "kubieke meter.")
elif volume_eddy < volume_thierry:
    print("Thierry heeft het grootste zwembad van de buurt.")
    print("Het zwembad heeft een volume van ", round(volume_thierry, 2), "kubieke meter.")
else:
    print("Eddy en Thierry hebben even grote zwembaden.")
    print("Beide zwembaden hebben een volume van ", round(volume_eddy, 2), "kubieke meter.")
