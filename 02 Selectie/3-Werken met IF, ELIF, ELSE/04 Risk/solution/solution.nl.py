# Invoer aanvaller
A1 = int(input("Geef de eerste worp van de aanvaller in: "))
A2 = int(input("Geef de tweede worp van de aanvaller in: "))
A3 = int(input("Geef de derde worp van de aanvaller in: "))

# Bepaal de hoogste en tweede hoogste worp van de aanvaller
# Eerste hoogste
A_eerste = max(A1, A2, A3)

# Tweede hoogste
# Bereken de som van alle worpen
A_som = A1 + A2 + A3
# Bereken de tweede hoogste door de hoogste en laagste worp af te trekken van de som
A_tweede = A_som - A_eerste - min(A1, A2, A3)

# Invoer verdediger
V1 = int(input("Geef de eerste worp van de verdediger in: "))
V2 = int(input("Geef de tweede worp van de verdediger in: "))

# Bepaal de hoogste en tweede hoogste worp van de verdediger
V_eerste = max(V1, V2)
V_tweede = min(V1, V2)

# Initialiseer verliezen
aanvaller_verlies = 0
verdediger_verlies = 0

# Vergelijk de hoogste worpen
if A_eerste > V_eerste:
    verdediger_verlies += 1
else:
    aanvaller_verlies += 1

# Vergelijk de tweede hoogste worpen
if A_tweede > V_tweede:
    verdediger_verlies += 1
else:
    aanvaller_verlies += 1

# Uitvoer
print("Verloren eenheden aanvaller:", aanvaller_verlies)
print("Verloren eenheden verdediging:", verdediger_verlies)
