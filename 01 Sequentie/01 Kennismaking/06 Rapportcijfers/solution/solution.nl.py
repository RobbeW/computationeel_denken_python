# Vraag de gebruiker om de score van drie toetsen in te voeren
toets_1 = float(input("Geef je resultaat voor toets 1: "))
toets_2 = float(input("Geef je resultaat voor toets 2: "))
toets_3 = float(input("Geef je resultaat voor toets 3: "))

# Bereken de totaalscore
totaalscore = toets_1 + toets_2 + toets_3

# Bereken het gemiddelde
gemiddelde = totaalscore / 3

# Bereken het percentage
percentage = gemiddelde * 5

# Print de totaalscore, het gemiddelde en het percentage naar het scherm
print("Totaal:", totaalscore)
print("Gemiddelde:", gemiddelde)
print("Percentage:", percentage)
