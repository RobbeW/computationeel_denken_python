# Vraag de gebruiker om massa en lengte
massa = float(input("Voer jouw massa in (in kg): "))
lengte = float(input("Voer jouw lengte in (in meter): "))

# Bereken de BMI
bmi = round(massa / (lengte ** 2), 2)

# Categoriseer de BMI
if bmi < 18.5:
    categorie = "ondergewicht"
elif 18.5 <= bmi < 25:
    categorie = "gezond"
elif 25 <= bmi < 30:
    categorie = "overgewicht"
else:
    categorie = "obesitas"

# Print de BMI en de bijhorende categorie
print("Jouw BMI bedraagt:", bmi)
print("Dit komt overeen met de categorie:", categorie)
