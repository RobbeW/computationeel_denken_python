# Vraag de gebruiker om input
tijd = float(input("Vul jouw totale rijtijd in (in uur): "))
kilometers = int(input("Vul jouw maandelijks gereden kilometers in: "))

# Bereken de kosten voor elk pakket
prepaid = 3.49 * tijd + 0.37 * kilometers + 0
coop = 0 * tijd + 0.33 * kilometers + 75

# Bepaal welk pakket het meest voordelig is
if prepaid <= coop:
    print("Prepaid rijbudget is het meest voordelig.")
    kosten = prepaid
else:
    print("Coop formule is het meest voordelig.")
    kosten = coop

# Print het resultaat
print("Je betaalt daarmee:", round(kosten,2), "euro.")
