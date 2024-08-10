# Vraag de gebruiker om naam en leeftijd
naam = input("Voer je naam in: ")
leeftijd = int(input("Voer je leeftijd in: "))

# Controleer of de leeftijd tussen 12 en 16 is
if 12 <= leeftijd <= 16:
    print(naam + ", je mag gratis binnen!")
else:
    print(naam + ", je moet een dagticket kopen van 35 euro.")
