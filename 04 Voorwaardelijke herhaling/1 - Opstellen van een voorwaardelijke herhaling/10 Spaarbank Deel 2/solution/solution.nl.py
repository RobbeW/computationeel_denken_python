# Vraag de gebruiker om het startbedrag en de jaarlijkse interest
bedrag = float(input("Voer het startbedrag in: "))
interest = float(input("Voer de jaarlijkse interest in: "))

# Bereken het bedrag op de rekening na elk jaar
i = 0
while bedrag < 2000:
    bedrag *= (100 + interest) / 100
    print(f"Na {i+1} jaar staat er € {round(bedrag, 2)} op de rekening.")
    i += 1
