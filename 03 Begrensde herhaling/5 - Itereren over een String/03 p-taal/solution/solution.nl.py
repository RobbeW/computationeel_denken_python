# Lees de zin in van de gebruiker
woord = input("Voor een woord in: ")

nieuw = ""
for teken in woord:
    if teken in "aeiou":
        nieuw += teken + "p" + teken
    else:
        nieuw += teken

print(nieuw)
