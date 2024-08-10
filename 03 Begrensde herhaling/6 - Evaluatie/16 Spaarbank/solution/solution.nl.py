# Vraag de gebruiker om het startbedrag en de jaarlijkse interest
bedrag = float(input("Voer het startbedrag in (tussen 500 en 1000): "))
interest = float(input("Voer de jaarlijkse interest in: "))

# Bereken het bedrag op de rekening na elk jaar
for i in range(5):
    bedrag *= (100 + interest) / 100
    print(f"Na {i+1} jaar staat er € {round(bedrag, 2)} op de rekening.")
