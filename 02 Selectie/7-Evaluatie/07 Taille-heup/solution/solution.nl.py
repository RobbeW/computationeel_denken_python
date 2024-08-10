# Lees de gegevens in
geslacht = input("Geef je biologische geslacht in (man/vrouw): ")
taille = float(input("Geef de omtrek van je taille in: "))
heup = float(input("Geef de omtrek van je heup in: "))

# verhouding berekenen
p = taille / heup
print("Je taille-heup verhouding is:", round(p, 2))

# selectie
if geslacht == "man":
    if p < 0.94:
        print("Laag risico op hart- en vaatziekten.")
    elif p <= 1.00:
        print("Verhoogd risico op hart- en vaatziekten.")
    else:
        print("Sterk verhoogd risico op hart- en vaatziekten.")
else:
    if p < 0.80:
        print("Laag risico op hart- en vaatziekten.")
    elif p <= 0.90:
        print("Verhoogd risico op hart- en vaatziekten.")
    else:
        print("Sterk verhoogd risico op hart- en vaatziekten.")
