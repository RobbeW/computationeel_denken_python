import random

# Genereer een willekeurig getal tussen 1 en 10
a = random.randint(1, 10)

# Bereken en print de tafel van het willekeurige getal
for i in range(1, 11):
    product = i * a
    print(i, "x", a, "=", product)
