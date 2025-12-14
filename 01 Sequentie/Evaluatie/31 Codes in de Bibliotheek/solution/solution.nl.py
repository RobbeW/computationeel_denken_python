# Invoer
titel = input("Geef de titel van het boek: ")
genre = input("Geef de genre-afkorting in: ")
kleur = input("Geef de kleurcode in: ")
nummer = input("Geef het viercijferige nummer in: ")
controle = input("Geef het controlegetal in (1 cijfer): ")

# Cataloguscode samenstellen
cataloguscode = genre + "-" + kleur + "-" + nummer + controle

# Uitvoer
print("Het boek met cataloguscode", cataloguscode, "heeft als titel:", titel + ".")
