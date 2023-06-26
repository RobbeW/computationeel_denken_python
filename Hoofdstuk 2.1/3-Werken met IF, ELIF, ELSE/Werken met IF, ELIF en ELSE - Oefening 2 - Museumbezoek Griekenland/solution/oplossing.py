# Vraag de gebruiker om hun naam en leeftijd
naam = input("Voer je naam in: ")
leeftijd = int(input("Voer je leeftijd in: "))

# Bepaal de toegangsprijs op basis van de leeftijd
if leeftijd <= 26:
    toegangsprijs = 0
    print(f"Hallo, {naam}. Je hebt gratis toegang tot het museum.")
elif leeftijd >= 65:
    toegangsprijs = 5
    print(f"Hallo, {naam}. Je moet {toegangsprijs} euro betalen voor de toegang tot het museum.")
else:
    toegangsprijs = 9
    print(f"Hallo, {naam}. Je moet {toegangsprijs} euro betalen voor de toegang tot het museum.")
