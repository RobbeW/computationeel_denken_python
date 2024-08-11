# Lees de zin en de letter in van de gebruiker
woord = input("Voer een zin in: ")
letter = input("Voer een letter in: ")

# Tel hoeveel keer de letter in de zin voorkomt
aantal = 0
for teken in woord:
    if teken == letter:
        aantal += 1

print(f"De letter {letter} komt {aantal} keer voor in {woord}.")
