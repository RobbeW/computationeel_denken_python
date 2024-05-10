# Initialiseren van variabelen
som = 0
aantal_getallen = 0
getallen_groter_dan_tien = 0

# Lus
flag = True
while flag:
    getal = float(input("Geef een getal in: "))
    
    if flag := getal != 0:
        # Voeg het getal toe aan de som
        som += getal

        # Verhoog het aantal getallen met 1
        aantal_getallen += 1

        # Verhoog het aantal getallen groter dan 10 als het getal groter is dan 10
        if getal > 10:
            getallen_groter_dan_tien += 1
    
# Print het aantal getallen, hun som, en het aantal getallen groter dan 10
print("Aantal ingevoerde getallen:", aantal_getallen)
print("Som van de ingevoerde getallen:", round(som, 1) )
print("Aantal getallen groter dan 10:", getallen_groter_dan_tien)
