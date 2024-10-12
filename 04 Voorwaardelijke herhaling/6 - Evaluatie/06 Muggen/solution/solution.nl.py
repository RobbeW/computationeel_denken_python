import math
# Vragen naar beginwaarden
aantal_muggen = int(input("Geef het aantal muggen in: "))  # Aantal volwassen muggen
aantal_larven = int(input("Geef het aantal larven in: "))  # Aantal larven
aantal_poppen = int(input("Geef het aantal poppen in: "))  # Aantal poppen
aantal_eitjes_per_mug = int(input("Geef het aantal eitjes in dat één mug legt: "))  # Eitjes per volwassen mug
aantal_weken = int(input("Geef het aantal weken in: "))  # Aantal weken om te simuleren

# Simulatie voor het opgegeven aantal weken
for week in range(aantal_weken):
    # Muggen leggen eitjes en die worden larven
    nieuwe_larven = aantal_muggen * aantal_eitjes_per_mug
    
    # Een deel van de larven wordt poppen (maar niet allemaal)
    nieuwe_poppen = aantal_larven // 2  # Laten we 50% van de larven overleven
    
    # Een groter deel van de poppen wordt muggen (minder sterfte)
    nieuwe_muggen = aantal_poppen // 1.5  # Ongeveer 2 op 3 poppen overleven
    
    # Update populaties voor de volgende week
    aantal_muggen = math.ceil(aantal_muggen + nieuwe_muggen)  # Muggen overleven en nieuwe muggen worden toegevoegd
    aantal_poppen = math.ceil(nieuwe_poppen)  # Overgebleven poppen
    aantal_larven = math.ceil(nieuwe_larven)  # Nieuwe larven

# Eindresultaat tonen
print("Er zijn", aantal_muggen, "muggen na week", aantal_weken)

