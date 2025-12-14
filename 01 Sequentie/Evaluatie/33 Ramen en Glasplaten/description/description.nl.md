## Gegeven:
Charlotte is een kunstzinnige architect en verwerkt in de huizen die ze ontwerpt zowel **cirkelvormige ramen** als **gelijkbenige driehoekige ramen**.

Om deze ramen te maken, koopt de aannemer bij GLASANDCO **vierkante glasplaten** met een bepaalde **oppervlakte** (in cm²).

Uit elke vierkante glasplaat wil men in het atelier twee vormen snijden:

1. een **cirkel** met de maximaal mogelijke straal die in het vierkant past;
2. een **scherphoekige gelijkbenige driehoek** die in het vierkant past, waarbij de **basis gelijk is aan één zijde van het vierkant**.

Charlotte wil daarom voor elke glasplaat berekenen:

- de **zijde** van het vierkant;
- de **maximale straal** en **oppervlakte** van de cirkel die in het vierkant past;
- de **maximale oppervlakte** van de scherphoekige gelijkbenige driehoek in het vierkant;
- de lengte van de **opstaande zijden** van die driehoek.  
  Tip: gebruik de **stelling van Pythagoras**.

## Gevraagd:
Schrijf een programma dat:

- vraagt: de **oppervlakte** van de vierkante glasplaat (in cm²);
- berekent: de **zijde** van het vierkant (afronden op 2 decimalen);
- berekent: de **maximale straal** van de cirkel die in het vierkant past (afronden op 1 decimaal);  
  tip: de diameter van de cirkel is gelijk aan de zijde van het vierkant;
- berekent: de **oppervlakte van de cirkel** (afronden op 2 decimalen);
- berekent: de **oppervlakte van de scherphoekige gelijkbenige driehoek** met basis = zijde van het vierkant, die binnen het vierkant past (afronden op 2 decimalen);  
  tip: de maximale hoogte is gelijk aan de zijde van het vierkant;
- berekent: de **lengte van de opstaande zijden** van die driehoek (afronden op 1 decimaal);  
  tip: gebruik Pythagoras op een rechthoekige driehoek met halve basis en de hoogte;
- drukt alle resultaten af in exact dezelfde zinnen als in het voorbeeld.

Je mag `import math` gebruiken.

## Voorbeeld

Voor invoer:
```text
600
```

Verschijnt er: 
```
De zijde van het vierkant is 24.49 cm.
De maximale straal van de cirkel is 12.2 cm.
De oppervlakte van de cirkel is 471.24 cm².
De oppervlakte van de gelijkbenige driehoek is 300.0 cm².
De opstaande zijden zijn 27.4 cm lang.
```