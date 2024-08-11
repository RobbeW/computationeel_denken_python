# Vraag de woorden
woord = input("Geef het eerste woord in: ")

# Controle of het een isogram is
is_isogram = True
nieuw = ""
for teken in woord:
    is_isogram = is_isogram and teken not in nieuw
    nieuw += teken

print(is_isogram)
