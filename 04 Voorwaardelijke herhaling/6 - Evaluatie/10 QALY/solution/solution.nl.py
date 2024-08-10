# Aantal levensfasen
n = int(input("Geef het aantal levensfasen in: "))

# berekeningen
leeftijd = 0
qaly = 0
for i in range(n):
    j = float(input("Hoe lang duurde deze periode? "))
    q = float(input("Wat was de levenkwaliteit? "))
    qaly += q * j
    leeftijd += j

# Weergave
print(f"Deze persoon van {round(leeftijd, 2)} jaar had een totale QALY van {round(qaly, 3)}")
