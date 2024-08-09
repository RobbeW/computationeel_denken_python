import math

# Vraag de gebruiker naar de lengte en hoogte van de muur
lengte_muur = float(input("Voer de lengte van de muur in (in meter): "))
hoogte_muur = float(input("Voer de hoogte van de muur in (in meter): "))

# Bereken het oppervlak van de muur
oppervlak_muur = lengte_muur * hoogte_muur

# Bereken het oppervlak van één rol behangpapier (breedte is omgezet naar meters)
oppervlak_behangpapier = 10 * (52 / 100)

# Bereken het aantal benodigde rollen behangpapier en rond naar boven af
aantal_rollen = math.ceil(oppervlak_muur / oppervlak_behangpapier)

# Print het berekende aantal benodigde rollen behangpapier op het scherm
print("Het aantal benodigde rollen behangpapier is", aantal_rollen, "rollen.")
