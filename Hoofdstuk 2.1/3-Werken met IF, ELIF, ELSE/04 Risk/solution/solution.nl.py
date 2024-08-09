# Invoer speler 1
P1_1 = int(input("Geef de eerste worp van speler 1 in: "))
P1_2 = int(input("Geef de tweede worp van speler 1 in: "))
P1_3 = int(input("Geef de derde worp van speler 1 in: "))

# Bepaalde hoogste en tweede hoogste worp
P1_eerste = max(P1_1, P1_2, P1_3)
P1_tweede = P1_1 + P1_2 + P1_3 - max(P1_1, P1_2, P1_3) - min(P1_1, P1_2, P1_3)

# Invoer speler 2
P2_1 = int(input("Geef de eerste worp van speler 2 in: "))
P2_2 = int(input("Geef de tweede worp van speler 2 in: "))

# Stel het aantal verloren eenheden in op 0
P1_verloren = 0

# Wijzig dit aantal, naargelang de worpen
if P1_eerste >= max(P2_1, P2_2):
    P1_verloren += 1

if P1_tweede >= min(P2_1, P2_2):
    P1_verloren += 1

# Uitvoer
print("Verloren eenheden aanvaller:", P1_verloren)
print("Verloren eenheden verdediging:", 2 - P1_verloren)
