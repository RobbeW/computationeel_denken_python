# Vnvoer vragen
woord = input("Geef een woord in: ")
# Welke klinkers zijn er?
klinkers = "aeiou"

# Bepaal het aantal dubbele klinkers
aantal = 0
for i in range(len(woord) - 1):
    char = woord[i]
    nchar = woord[i + 1]
    if char == nchar and char in klinkers:
        aantal += 1

# Uitvoer
print(aantal)
