# Invoer vragen
x = int(input("Geef de datalimiet in: "))
n = int(input("Geef het aantal maanden in: "))

# Berekenen van het verbruik
som = x
for i in range(n):
    used = int(input("Geef het verbruik van deze maand in: "))
    som += x - used
    
# Weergave
print(f"Beschikbaar: {som} MB")
