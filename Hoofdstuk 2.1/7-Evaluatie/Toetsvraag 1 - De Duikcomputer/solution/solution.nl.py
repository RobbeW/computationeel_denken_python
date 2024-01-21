# Vraag de gebruiker om de totale duiktijd
totaal_duiktijd = int(input("Voer jouw totale duiktijd in: "))

# Controleer de invoer en druk de juiste boodschap af
if totaal_duiktijd < 30:
    print("Je hoeft niet te stoppen op 3 meter.")
elif totaal_duiktijd < 40:
    print("Je moet vijf minuten stoppen op 3 meter.")
elif totaal_duiktijd < 50:
    print("Je moet tien minuten stoppen op 3 meter.")
else:
    print("Je moet twaalf minuten stoppen op 3 meter.")
