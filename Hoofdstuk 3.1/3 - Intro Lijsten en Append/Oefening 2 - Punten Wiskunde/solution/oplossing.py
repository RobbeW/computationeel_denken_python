import random

# Klaslijst met namen van studenten
Klas = ["Arn", "Belle", "Daan", "Emma", "Tessa", "Tom", "Jesse", "Tarik", "Noah", "Lyssa", "Dinah", "Noor"]

# Drie lege lijsten om de punten voor algebra, meetkunde en statistiek op te slaan
Algebra = []
Meetkunde = []
Statistiek = []

# Itereren over de klaslijst
for student in Klas:
    # Genereer de punten voor algebra, meetkunde en statistiek
    algebra_punten = random.randint(0, 20)
    meetkunde_punten = random.randint(0, 20)
    statistiek_punten = random.randint(0, 20)
    
    # Voeg de punten toe aan de betreffende lijsten
    Algebra.append(algebra_punten)
    Meetkunde.append(meetkunde_punten)
    Statistiek.append(statistiek_punten)

# Bereken en print het percentage voor elke student
for i in range(len(Klas)):
    totaal_punten = Algebra[i] + Meetkunde[i] + Statistiek[i]
    percentage = round((totaal_punten / 60) * 100,2)  # aangezien de totale score voor elk vak 20 is
    print("Het percentage voor", Klas[i], "is", percentage, "%.")
