# Vraag de gebruiker om de scores voor de drie toetsen
score1 = int(input("Voer de score van toets 1 in (op 20): "))
score2 = int(input("Voer de score van toets 2 in (op 20): "))
score3 = int(input("Voer de score van toets 3 in (op 20): "))

# Bereken het totale percentage en geef dit weer
totaal_score = score1 + score2 + score3
percentage = (totaal_score / 60) * 100

print("Je hebt", round(percentage, 1), "% behaald.")

# Controleer of de gebruiker voor elke toets minstens de helft van de punten heeft behaald
if score1 >= 10 and score2 >= 10 and score3 >= 10:
    # Bepaal de beoordeling op basis van het behaalde percentage
    if percentage > 67:
        print("Beoordeling: onderscheiding.")
    else:
        print("Beoordeling: geslaagd.")
else:
    # Deze regel is aangepast om duidelijk te maken dat de student niet geslaagd is
    # als een of meer scores lager dan 10 zijn.
    print("Beoordeling: niet geslaagd.")
