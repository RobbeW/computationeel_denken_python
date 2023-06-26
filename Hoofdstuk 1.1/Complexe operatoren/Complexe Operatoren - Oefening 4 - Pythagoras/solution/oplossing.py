# Vraag de gebruiker naar de lengtes van de twee kortste zijden
a = float(input("Voer de lengte van de eerste zijde in: "))
b = float(input("Voer de lengte van de tweede zijde in: "))

# Bereken de lengte van de hypotenusa
c = (a ** 2 + b ** 2) ** 0.5

# Print de lengte van de hypotenusa
print("De lengte van de hypotenusa is:", c, "centimeter.")
