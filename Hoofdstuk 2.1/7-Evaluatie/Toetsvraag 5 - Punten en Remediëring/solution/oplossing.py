# Lees de score op 10 in voor wiskunde
score = float(input("Voer jouw punt in: "))

# Beoordeel de score en print de bijbehorende feedback
if score >= 8:
    print("Proficiat!")
elif 6 <= score < 8:
    print("Goed gewerkt!")
else:
    print("Oei, het lijkt ons aangewezen als je deze leerstof nog eens doorneemt via een inhaalles of remediëring.")
