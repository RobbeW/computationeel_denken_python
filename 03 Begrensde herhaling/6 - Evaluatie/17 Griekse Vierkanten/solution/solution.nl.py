import math

# Invoer vragen
n = int(input("Geef het aantal iteraties: "))
A = float(input("Geef de eerste oppervlakte in: "))

# Uitvoer
z = math.sqrt(A)
print(f"De startzijde meet {round(z, 2)} cm en de oppervlakte was {round(A, 2)} cm².")
for i in range(n):
    A /= 2
    z = math.sqrt(A)
    
    print(f"In iteratie {i+1} meet de zijde {round(z, 2)} cm en bedraagt de oppervlakte {round(A, 2)} cm².")
