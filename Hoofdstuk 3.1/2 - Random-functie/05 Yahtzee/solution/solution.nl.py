import random

# Variabele om de som van de worpen bij te houden
aantal = 0

n = int(input("Geef het aantal worpen in: "))

# We doen dit een aantal keer
for _ in range(n):
    # Genereer twee willekeurige getallen tussen 1 en 6
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    d = random.randint(1, 6)
    e = random.randint(1, 6)
    
    m = min(a,b,c,d,e)
    M = max(a,b,c,d,e)
    # Enkel als 
    if (m == 1 and M == 5) or (m == 2 and M == 6):
        # controleren of er geen twee dezelfde tussenzitten
        if not( a == b or a == c or a == d or a == e or b == c or b == d or b == e or c == d or c == e or d == e):
            aantal += 1

# Bereken het gemiddelde
kans = round( aantal / n * 100, 2)

print()
# Print het gemiddelde van de worpen naar het scherm
print(f"De kans op grote straat is ongeveer {kans} %")

# echte kans is  2 * (5 * 4 * 3 * 2 * 1) / (6**5) = ca 3.09%