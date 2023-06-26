import random

# Variabele om de som van de worpen bij te houden
som = 0

# We doen dit veertig keer
for i in range(40):
    # Genereer twee willekeurige getallen tussen 1 en 6
    worp1 = random.randint(1, 6)
    worp2 = random.randint(1, 6)
    
    # Voeg de resultaten van de worpen toe aan de som
    som += worp1 + worp2

# Bereken het gemiddelde
gemiddelde = som / 40

# Print het gemiddelde van de worpen naar het scherm
print("Het gemiddelde van de 40 worpen is", gemiddelde)
