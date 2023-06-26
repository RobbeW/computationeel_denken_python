# Vraag de gebruiker naar een getal
a = int(input("Voer een getal a in: "))

# Controleer of a groter is dan 20
if a > 20:
    b = a ** 2 - 2 * a
else:
    b = a ** 2 + 2 * a

print("Het berekende getal b is:", b)
