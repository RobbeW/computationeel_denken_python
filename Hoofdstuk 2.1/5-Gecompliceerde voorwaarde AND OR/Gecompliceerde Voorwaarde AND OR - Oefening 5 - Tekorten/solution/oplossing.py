# Vraag de gebruiker om de scores voor de twee toetsen
score1 = int(input("Voer de score van de eerste test in: "))
score2 = int(input("Voer de score van de tweede test in: "))

# Beoordeel de scores
if score1 > 50 and score2 > 50:
    print("Beoordeling:", "oké")
elif score1 > 50 and score2 <= 50 or score1 <= 50 and score2 > 50:
    print("Beoordeling:", "1 tekort")
else:
    print("Beoordeling:", "niet oké")
