# Lees de zin en de letter in van de gebruiker
zin = input("Voer een zin in: ")
letter = input("Voer een letter in: ")

# Tel hoeveel keer de letter in de zin voorkomt
aantal = zin.count(letter)

# Print het aantal keren dat de letter voorkomt in de zin
print("De letter", letter, "komt", aantal, "keer voor in de zin.")
