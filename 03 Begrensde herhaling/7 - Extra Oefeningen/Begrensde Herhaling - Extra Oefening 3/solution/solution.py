
# Maak een lege lijst voor de namen
namenlijst = []

# Vraag aan de leerkracht het aantal leerlingen in de klas
aantal_leerlingen = int(input("Hoeveel leerlingen zijn er? "))

# Voeg het aantal leerlingen toe aan de lijst
for i in range(aantal_leerlingen):
    naam = input("Voer de naam in van leerling " + str(i + 1) + ": ")
    namenlijst.append(naam)

# Begrensde herhaling om elke naam in de lijst af te drukken met het aantal letters
for naam in namenlijst:
    aantal_letters = len(naam)
    print(naam + " heeft " + str(aantal_letters) + " letters.")
