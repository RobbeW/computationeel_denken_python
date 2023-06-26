# Lees de zin in van de gebruiker
zin = input("Voer een zin in: ")

# Definieer de klinkers
klinkers = 'aeiouAEIOU'

# Vervang elke klinker door een 'x'
for k in klinkers:
    zin = zin.replace(k, 'x')

# Print de geconverteerde zin
print("De geconverteerde zin is: ", zin)
