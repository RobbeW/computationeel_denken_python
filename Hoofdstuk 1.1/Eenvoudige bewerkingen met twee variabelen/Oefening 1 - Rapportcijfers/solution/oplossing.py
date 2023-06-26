# Vraag de gebruiker om de score van drie toetsen in te voeren
toets_1 = float(input("toets_1 = "))
toets_2 = float(input("toets_2 = "))
toets_3 = float(input("toets_3 = "))

# Bereken de totaalscore
totaalscore = toets_1 + toets_2 + toets_3

# Bereken het gemiddelde
gemiddelde = totaalscore / 3

# Bereken het percentage
percentage = gemiddelde * 5

# Print de totaalscore, het gemiddelde en het percentage naar het scherm
print(totaalscore)
print(gemiddelde)
print(percentage)
