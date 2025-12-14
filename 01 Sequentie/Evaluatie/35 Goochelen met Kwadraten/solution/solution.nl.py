# Invoer
n = int(input())

# Cijfers bepalen
d1 = n // 1000
d2 = (n // 100) % 10
d3 = (n // 10) % 10
d4 = n % 10

# Kwadraten achter elkaar zetten
nieuw = str(d1 * d1) + str(d2 * d2) + str(d3 * d3) + str(d4 * d4)

# Uitvoer
print(nieuw)