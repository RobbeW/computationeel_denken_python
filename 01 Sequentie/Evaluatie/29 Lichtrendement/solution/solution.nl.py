# Invoer vragen
vermogen = float( input("Geef het vermogen van de lamp? ") )
lichtstroom = int( input("Geef de lichtstroom van de lamp? ") )

# Verwerking
rendement = lichtstroom / vermogen

# Weergeven op het scherm
print("Het lichtrendement is", round(rendement, 2), "lumen per watt.")
