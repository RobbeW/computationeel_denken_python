# Initialiseren van variabelen
totaal_score = 0.0
aantal_leerlingen = 0

# Lus
flag = True
while flag:
    # Vraag de score
    score = float( input( "Geef de score van de leerling op 20 in: " ) )
    if flag := score > 0:
        # Voeg de score toe aan de totale score
        totaal_score += score
        # Verhoog het aantal leerlingen met 1
        aantal_leerlingen += 1
    
# Bereken het gemiddelde
gemiddelde = totaal_score / aantal_leerlingen

# Print het aantal leerlingen en het gemiddelde
print("Aantal leerlingen:", aantal_leerlingen)
print("Klasgemiddelde op 20:", round(gemiddelde, 1))
