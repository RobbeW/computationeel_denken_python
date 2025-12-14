import math

# Invoer:
oppervlakte_vierkant = float(input("Geef de oppervlakte van de vierkante glasplaat in (cm²): "))

# Zijde van het vierkant
zijde = math.sqrt(oppervlakte_vierkant)

# Cirkel die maximaal in het vierkant past
straal = zijde / 2
oppervlakte_cirkel = math.pi * straal * straal

# Gelijkbenige driehoek 
oppervlakte_driehoek = (zijde * zijde) / 2

# Opstaande zijden 
opstaande_zijde = math.sqrt((zijde / 2) * (zijde / 2) + zijde * zijde)

# Afronden voor weergave:
zijde_afgerond = round(zijde, 2)
straal_afgerond = round(straal, 1)
oppervlakte_cirkel_afgerond = round(oppervlakte_cirkel, 2)
oppervlakte_driehoek_afgerond = round(oppervlakte_driehoek, 2)
opstaande_zijde_afgerond = round(opstaande_zijde, 1)

# Uitvoer:
print("De zijde van het vierkant is", zijde_afgerond, "cm.")
print("De maximale straal van de cirkel is", straal_afgerond, "cm.")
print("De oppervlakte van de cirkel is", oppervlakte_cirkel_afgerond, "cm².")
print("De oppervlakte van de gelijkbenige driehoek is", oppervlakte_driehoek_afgerond, "cm².")
print("De opstaande zijden zijn", opstaande_zijde_afgerond, "cm lang.")
