# Vraagt de gebruik om een bedrag
bedrag = int( input( "Voer het te betalen bedrag in euro's in: " ) )

# Bepaalt het aantal briefjes van 50 euro
aantal_vijftig = bedrag // 50 # dit berekent het quotiënt zonder rest. 
restbedrag = bedrag % 50      # dit berekent de rest zonder quotiënt en kent deze toe aan de variabele restbedrag. 
                              # vervolgens kan je verder werken met dit restbedrag