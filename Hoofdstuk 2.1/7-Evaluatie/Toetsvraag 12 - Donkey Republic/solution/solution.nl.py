import math

# Vraag de gebruiker om input
tijd = float(input("Vul jouw dagelijkse rijtijd in (in uur): "))

# Bereken de kosten voor elk pakket
just_ride = 3.3 * math.sqrt(tijd)
daily_rider = 1
if tijd > 1:
    daily_rider = 1 + 3.3 * math.sqrt(tijd - 1)

# Bepaal welk pakket het meest voordelig is
if just_ride <= daily_rider:
    print("Just Ride is het meest voordelig.")
    kosten = just_ride
else:
    print("Daily Rider is het meest voordelig.")
    kosten = daily_rider

# Print het resultaat
print("Je betaalt daarmee:", round(kosten,2), "euro per dag.")
