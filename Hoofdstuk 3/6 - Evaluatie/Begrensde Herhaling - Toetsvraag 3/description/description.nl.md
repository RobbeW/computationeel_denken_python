# Toetsvraag 3 - Begrensde Herhaling – Griekse Vierkanten (Deel II)

## Gegeven: 
* Er zijn vijf vierkanten (ABCD, EFGH, IJKL, MNOP, QRST). 
* Het kleinste vierkant ABCD heeft een zijde van 5 meter. 
* Elk daaropvolgend vierkant heeft een oppervlakte die tweemaal de oppervlakte is van het voorgaande vierkant.


## Gevraagd:

* Schrijf een programma dat de **oppervlakte van het vierkant** en de **lengte van de zijden** van elk van de vijf vierkanten berekent;
* Print de afmetingen (lengte en oppervlakte) telkens naar het scherm in een verzorgde volzin.
* Rond de lengte van de zijdes en de oppervlaktes telkens af tot **twee decimalen.**
* Gebruik de `round-functie`. 

## Uitvoer: 

```
De lengte van de zijde van vierkant ABCD is ... meter en de oppervlakte is ... vierkante meter.
De lengte van de zijde van vierkant EFGH is ... meter en de oppervlakte is ... vierkante meter.
...

```

## Tips: 

* Start met een variabele voor de lengte van de zijde van het kleinste vierkant (ABCD), welke 5 is.
* Gebruik een `lijst` om de namen van de vierkanten eenvoudig te integreren in de output.
* Gebruik een `for-loop` om door elk van de vijf vierkanten te itereren.
* In elke iteratie, bereken de **oppervlakte van het huidige vierkant** en de **lengte van de zijde van het vierkant.**
* Print de **lengte van de zijde** en de **oppervlakte van het huidige vierkant** naar het scherm.
* Update de lengte van de zijde voor de volgende iteratie.