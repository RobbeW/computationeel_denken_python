# Vraag de gebruiker om de scores voor de twee toetsen
score1 = int( input("Voer de score van de eerste test in: " ) )
score2 = int( input("Voer de score van de tweede test in: " ) )

# Beoordeel de scores
print()
if score1 >= 50 and score2 >= 50:
    print("Beoordeling:", "oké")
elif score1 < 50 and score2 < 50:
    print("Beoordeling:", "niet oké")
else:
    print("Beoordeling:", "één tekort")
