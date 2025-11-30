import math

# Vraag de zijde van het vierkant:
zijde = float(input("Geef de zijde van het vierkant in (cm): "))

# Oppervlakte van het vierkant:
oppervlakte = zijde * zijde

# Straal van de cirkel met dezelfde oppervlakte:
straal = math.sqrt(oppervlakte / math.pi)

# Afronden voor de weergave:
oppervlakte_afgerond = round(oppervlakte, 2)
straal_afgerond = round(straal, 1)

# Uitvoer:
print("De oppervlakte van zowel de cirkel als die van het vierkant zijn", oppervlakte_afgerond, "cm².")
print("De straal van de cirkel is", straal_afgerond, "cm.")
