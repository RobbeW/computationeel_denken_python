# Kamertemperatuur en doeltemperatuur
huidige_temperatuur = float(input("Geef de kamertemperatuur in: "))
doel_temperatuur = 180.0

# Tijd teller
tijd = 0

while huidige_temperatuur < doel_temperatuur:
    # Print de huidige tijd en temperatuur
    if tijd == 1:
        print("Er is 1 minuut voorbij.")
    elif tijd > 1:
        print("Er zijn", tijd, "minuten voorbij.")
    print("De huidige temperatuur van de oven is", round(huidige_temperatuur, 2), "graden.")
    
    # Verhoog de temperatuur en tijd
    huidige_temperatuur *= 1.17
    tijd += 1

# Print de eindtijd
print("De oven is voorverwarmd na", tijd, "minuten.")
