# Lees het woord in van de gebruiker
woord = input("Voer een woord in: ")

# Bereken de lengte van het woord
lengte = len(woord)

# Creëer een lege string om het omgekeerde woord op te slaan
omgekeerd_woord = ""

# Gebruik een for-lus om door het woord heen te gaan, van achter naar voren
for i in range(lengte-1, -1, -1):
    omgekeerd_woord = omgekeerd_woord + woord[i]

# Print het omgekeerde woord
print("Het omgekeerde woord is: ", omgekeerd_woord)
