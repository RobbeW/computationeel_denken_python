# Vraag de gebruiker om massa en lengte
massa = float(input("Voer jouw massa in (in kg): "))
lengte = float(input("Voer jouw lengte in (in meter): "))

# Bereken de BMI
lengte /= 100
bmi = round(massa / (lengte ** 2), 2)

# Categoriseer de BMI met behulp van 'and' en 'or'
if bmi <= 18.5:
    categorie = "ondergewicht"
elif bmi > 18.5 and bmi <= 25:
    categorie = "gezond"
elif bmi > 25 and bmi <= 30:
    categorie = "overgewicht"
else:
    categorie = "obesitas"

# Print de BMI en de bijhorende categorie
print("Jouw BMI bedraagt:", bmi)
print("Dit komt overeen met de categorie:", categorie)
