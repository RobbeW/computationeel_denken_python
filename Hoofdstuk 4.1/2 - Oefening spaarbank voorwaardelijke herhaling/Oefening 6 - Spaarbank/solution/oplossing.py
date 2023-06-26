import random

# Genereer een willekeurig startbedrag tussen 500 en 1000
startbedrag = random.randint(500, 1000)

# Initialiseer een teller voor het aantal jaren
jaar = 0

# Het huidige bedrag is het startbedrag
huidig_bedrag = startbedrag

# Print het startbedrag
print("Simon is begonnen met een bedrag van", startbedrag, ".")

# Zolang het huidige bedrag minder dan 2000 is
while huidig_bedrag < 2000:
    # Verhoog het huidige bedrag met de rente (2.4% van het huidige bedrag)
    huidig_bedrag = round(huidig_bedrag * 1.024,2)

    # Verhoog de teller voor het aantal jaren
    jaar += 1

    # Print het huidige bedrag na dit jaar
    print("Na", jaar, "jaar is het bedrag op de rekening", huidig_bedrag, "euro.")

# Print het eindbedrag en het aantal jaren
print("Na", jaar, "jaar sparen met een jaarlijkse interest van 2.4%, is het bedrag op de rekening gegroeid tot", huidig_bedrag, "euro.")
