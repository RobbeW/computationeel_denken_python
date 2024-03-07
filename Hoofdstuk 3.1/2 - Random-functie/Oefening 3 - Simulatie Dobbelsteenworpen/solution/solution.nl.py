import random

# Variabele om de som van de worpen bij te houden
som = 0

n = int(input("Geef het aantal worpen in: "))

# We doen dit veertig keer
for _ in range(n):
    # Genereer twee willekeurige getallen tussen 1 en 6
    worp1 = random.randint(1, 6)
    worp2 = random.randint(1, 6)
    
    # Voeg de resultaten van de worpen toe aan de som
    som += worp1 + worp2

# Bereken het gemiddelde
gemiddelde = round( som / n, 2)

# Print het gemiddelde van de worpen naar het scherm
print("Het gemiddelde bij", n, "worpen is", gemiddelde)
