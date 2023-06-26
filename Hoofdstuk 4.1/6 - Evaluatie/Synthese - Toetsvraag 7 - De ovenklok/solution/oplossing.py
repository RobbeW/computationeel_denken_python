# Kamertemperatuur en doeltemperatuur
huidige_temperatuur = 20.0
doel_temperatuur = 180.0

# Tijd teller
tijd = 0

while huidige_temperatuur < doel_temperatuur:
    # Print de huidige tijd en temperatuur
    print(str(tijd) + " minuten voorbij. De huidige temperatuur van de oven is " + str(round(huidige_temperatuur, 2)) + " graden.")
    
    # Verhoog de temperatuur en tijd
    huidige_temperatuur += huidige_temperatuur * 0.17
    tijd += 1

# Print de eindtijd
print("De oven is voorverwarmd na " + str(tijd) + " minuten.")
