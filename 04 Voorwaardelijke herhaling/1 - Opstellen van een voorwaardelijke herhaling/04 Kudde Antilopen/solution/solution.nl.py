import math
# Initialiseer de grootte van de kudde en het aantal jaren
kudde = int(input( "Geef het aantal antilopen in: "))
jaar = 0

# Zolang de kudde kleiner is dan 300...
while kudde < 350:
    # Verhoog het jaar met 1
    jaar += 1
    # Verhoog de grootte van de kudde met 6%
    kudde *= 1.06
    kudde = math.floor(kudde)
    # Print de grootte van de kudde
    print("Jaar", jaar, ":", round(kudde), "antilopen")

print("Er zullen minstens 350 antilopen zijn na", jaar, "jaar.")
