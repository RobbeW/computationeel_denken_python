# Invoer vragen
aantal_min = int( input("Hoeveel minuten zal je met de Concorde vliegen? ") )

# Verwerking
aantal_uur = aantal_min / 60
afstand = aantal_uur * 1740

# Weergeven op het scherm
print("Als je", aantal_min, "minuten vliegt, dan heb je", afstand, "km afgelegd.")
