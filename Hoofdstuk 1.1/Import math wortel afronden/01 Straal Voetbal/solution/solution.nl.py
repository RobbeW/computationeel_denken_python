import math

# Vraag de gebruiker naar de omtrek van de cirkel
omtrek = float(input("De omtrek van de cirkel bedraagt: "))

# Bereken de straal van de cirkel
straal = omtrek / (2 * math.pi)

# Rond de straal af op 2 decimalen
straal_afgerond = round(straal, 2)

# Print het resultaat
print("De straal van de cirkel is", straal_afgerond, "cm.")
