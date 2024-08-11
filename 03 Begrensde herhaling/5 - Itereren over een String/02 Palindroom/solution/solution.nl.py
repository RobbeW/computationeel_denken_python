# Lees de zin in van de gebruiker
woord = input("Geef een woord (enkel kleine letters): ")

# Bepaal het omgekeerde woord
omgekeerd = ""
for teken in woord:
    omgekeerd = teken + omgekeerd

# Weergave
print(omgekeerd == woord)
