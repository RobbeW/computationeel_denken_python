# Invoer vragen
voornaam = input("Voer je voornaam in: ")
beginlengte = int(input("Voer de beginlengte in (in cm): "))
restlengte = int(input("Voer de resterende lengte in (in cm): "))

# Berekening
aantal_uur = beginlengte - restlengte

# Weergeven op het scherm
print("Monnik", voornaam + ": er is ondertussen", aantal_uur, "u verstreken.")
