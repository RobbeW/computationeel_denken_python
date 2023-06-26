import math

# Vraag de gebruiker om input
kilometers = int(input("Vul jouw maandelijks gereden kilometers in: "))
tijd = float(input("Vul jouw totale rijtijd in (in uur): "))

# Bereken de kosten voor elk pakket
tijd = math.ceil(tijd)  # de tijd naar boven afronden, omdat we rekenen per begonnen uur
kosten_pakket1 = tijd * 6 + kilometers * 0.34
kosten_pakket2 = 10 + tijd * 4 + kilometers * 0.29
kosten_pakket3 = 25 + tijd * 3 + kilometers * 0.24

# Bepaal welk pakket het meest voordelig is
if kosten_pakket1 < kosten_pakket2 and kosten_pakket1 < kosten_pakket3:
    voordeligste_pakket = 1
    kosten = kosten_pakket1
elif kosten_pakket2 < kosten_pakket1 and kosten_pakket2 < kosten_pakket3:
    voordeligste_pakket = 2
    kosten = kosten_pakket2
else:
    voordeligste_pakket = 3
    kosten = kosten_pakket3

# Print het resultaat
print("Pakket", voordeligste_pakket, "is het meest voordelig.")
print("Je betaalt daarmee:", round(kosten,2), "euro.")
