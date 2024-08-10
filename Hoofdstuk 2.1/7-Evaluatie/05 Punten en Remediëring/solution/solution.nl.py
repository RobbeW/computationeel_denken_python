# Lees de score in
score = float(input("Voer jouw punt in: "))
totaal = float(input("Voer het totaal in in: "))

perc = score / totaal

# Beoordeel de score en print de bijbehorende feedback
if perc >= 0.8:
    print("Proficiat!")
elif perc >= 0.6:
    print("Goed gewerkt!")
else:
    print("Oei, het lijkt ons aangewezen als je deze leerstof nog eens doorneemt via een inhaalles of remediëring.")
