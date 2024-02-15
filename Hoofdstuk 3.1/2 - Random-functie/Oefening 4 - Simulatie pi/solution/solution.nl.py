import random
import math

# Variabele om het aantal bij te houden
aantal = 0

n = int(input("Geef het aantal simulaties in: "))

# We doen dit zoveel keer
for _ in range(n):
    # Genereer twee willekeurige getallen tussen 1 en 6
    x = random.randint(-100, 100) / 100
    y = random.randint(-100, 100) / 100
    
    if math.sqrt(x**2+y**2) < 1:
        aantal += 1

# Bereken de schatting
schatting = round( 4 * aantal / n, 5)

# Geef de schatting weer
print("Bij", n, "simulaties bedraagt de schatting voor pi ongeveer:", schatting)
