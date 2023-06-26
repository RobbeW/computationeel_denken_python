# Initialiseer de grootte van de kudde en het aantal jaren
kudde = 120
jaar = 0

# Zolang de kudde kleiner is dan 300...
while kudde < 300:
    # Verhoog het jaar met 1
    jaar += 1
    # Verhoog de grootte van de kudde met 6%
    kudde *= 1.06
    # Print de grootte van de kudde
    print("Jaar", jaar, ":", round(kudde), "antilopen")

print("Er zullen minstens 300 antilopen zijn na", jaar, "jaar.")
