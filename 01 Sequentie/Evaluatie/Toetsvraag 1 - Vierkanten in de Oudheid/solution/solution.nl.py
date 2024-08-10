import math

# Vraag de gebruiker om de lengte van een zijde van vierkant ABCD
zijde_abcd = float(input("Voer de lengte van een zijde van vierkant ABCD in (in meter): "))

# Bereken de oppervlakte van vierkant ABCD
oppervlakte_abcd = zijde_abcd ** 2

# De oppervlakte van vierkant PQRS is het dubbel van vierkant ABCD
oppervlakte_pqrs = 2 * oppervlakte_abcd

# De lengte van een zijde van vierkant PQRS kan berekend worden door de vierkantswortel van de oppervlakte te nemen
zijde_pqrs = math.sqrt(oppervlakte_pqrs)

# Rond de waarden af tot twee decimalen en sla ze op in nieuwe variabelen
oppervlakte_pqrs_afgerond = round(oppervlakte_pqrs, 2)
zijde_pqrs_afgerond = round(zijde_pqrs, 2)

# Print de berekende oppervlakte en zijde van vierkant PQRS naar het scherm in verzorgde volzinnen
print("De oppervlakte van vierkant PQRS is", oppervlakte_pqrs_afgerond, "m².")
print("De lengte van een zijde van vierkant PQRS is", zijde_pqrs_afgerond, "m.")
