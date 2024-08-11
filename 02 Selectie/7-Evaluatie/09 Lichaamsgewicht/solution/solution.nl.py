# Vraag de leeftijd
leeftijd = int(input("Geef de leeftijd in maanden in: "))

# Lichaamsmassa
if leeftijd < 12:
    m = 1/2 * leeftijd + 4
    print("De ideale lichaamsmassa is", round(m, 1), "kg.")
elif leeftijd <= 12*10:
    leeftijd = leeftijd / 12
    m = 2 * leeftijd + 10
    print("De ideale lichaamsmassa is", round(m, 1), "kg.")
else: 
    print("Dit kind is te oud om de formule van Leffler te gebruiken.")
