# Lees de zin in van de gebruiker
zin = input("Voer een zin in: ")

# Definieer de klinkers
klinkers = 'aeiouAEIOU'

# Vervang elke klinker door twee van hetzelfde
for k in klinkers:
    zin = zin.replace(k, k*2)

# Print de geconverteerde zin
print("De geconverteerde zin is: ", zin)
