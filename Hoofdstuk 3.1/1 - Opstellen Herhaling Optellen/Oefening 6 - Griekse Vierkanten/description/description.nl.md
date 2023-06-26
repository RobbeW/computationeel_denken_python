## Gegeven: 
Het Grieks vierkant is een vierkant bestaande uit vier identieke kleinere vierkanten. De oppervlakte van elk kleiner vierkant is een vierde van het omliggende vierkant. 

Het grootste vierkant heeft een oppervlakte van 144 vierkante meter. 


## Gevraagd: 
Schrijf een programma dat de `oppervlakte` en de `lengte van de zijde` van elkeen van de vier vierkanten berekent. 

## Invoer: 
```
De oppervlakte, in vierkante meter, van vierkant 1 is: 144

```

## Uitvoer: 
```
De lengte van de zijde van vierkant 1 is ... meter.
De oppervlakte van vierkant 2 ... vierkante meter.
De lengte van de zijde van vierkant 2 is ... meter.
De oppervlakte van vierkant 3 ... vierkante meter.
De lengte van de zijde van vierkant 3 is ... meter.
De oppervlakte van vierkant 4 ... vierkante meter.
De lengte van de zijde van vierkant 4 is ... meter.

```

{: .callout.callout-success}
>## Tips: 
>* De oppervlakte van elk kleiner vierkant kan worden berekend door de oppervlakte van het grote vierkant te delen door 4.
>* De lengte van de zijde van elk kleiner vierkant kan worden berekend door de **wortel** te nemen van de oppervlakte van het kleinere vierkant. 
>* Gebruik hiervoor de `math.sqrt()-functie` uit de `math module`. 
>* Vergeet niet om de math module eerst te importeren met `import math`.
