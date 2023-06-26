klaslijst = []

leerling = input('Geef jouw naam in: ')
while leerling != "STOP":
    klaslijst.append(leerling)
    leerling = input('Geef jouw naam in: ')

print("De klaslijst:", klaslijst)
print("Het totaal aantal leerlingen is", len(klaslijst), ".")
