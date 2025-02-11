import math

# Invoer vragen
lengte_zijde = float(input("Geef de zijde in (in cm): "))
aantal_iteraties = int(input("Geef de iteratie in: "))


# Aantal segmenten start op 1
totaal_segmenten = 1 
print("De startlengte was", round(totaal_segmenten * lengte_zijde, 2), "cm.")


# Iteraties uitvoeren
for i in range(aantal_iteraties):
    lengte_zijde = lengte_zijde / math.sqrt(2)  # Deel de zijde door √2
    totaal_segmenten = totaal_segmenten * 2  
    print("In iteratie", i + 1, "is de lengte van de draakkromme", round(totaal_segmenten * lengte_zijde, 2), "cm.")
