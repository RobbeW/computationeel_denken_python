# Invoer vragen
massa = float( input("Geef de massa in gram in? ") )
volume = float( input("Geef de het volume in dm³ in? ") )

# Verwerking
dichtheid = massa / (volume / 1000)

# Weergeven op het scherm
print("De massadichtheid bedraagt", round(dichtheid, 3), "kg / m³.")
