# Vraag naar de kaarten
kaarten = input("Geef de wetenschappelijke kaarten in: ")

# Tel de kaarten
aantal_P = 0
aantal_S = 0
aantal_T = 0
for char in kaarten:
    if char == "T":
        aantal_T += 1
    elif char == "P":
        aantal_P += 1
    else:
        aantal_S += 1

# Bereken de score
score = aantal_S**2 + aantal_P**2 + aantal_T**2
score += min(aantal_S, aantal_P, aantal_T) * 7

# Weergave
print(score)
