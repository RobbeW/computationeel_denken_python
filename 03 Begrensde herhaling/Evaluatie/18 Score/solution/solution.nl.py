# Vraag naar de antwoorden
response = input("Geef de antwoordenregel in: ")

# Bepaal de score
score = 0
teller = 0
for char in response:
    if char == "J":
        teller += 1
        score += teller
    else:
        teller = 0

# Weergave van de score
print(score)
