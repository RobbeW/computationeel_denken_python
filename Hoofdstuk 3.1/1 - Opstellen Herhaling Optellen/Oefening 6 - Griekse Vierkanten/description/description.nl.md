## Gegeven
Plato bestudeerde vierkanten opgebouwd uit vier identieke kleinere vierkanten. De oppervlakte van elk kleiner vierkant is een vierde van het omliggende vierkant. 

![De vierkanten van Plato.](media/image.png "De vierkanten van Plato.."){:data-caption="De vierkanten van Plato." .light-only width="30%"}

![De vierkanten van Plato.](media/image_dark.png "De vierkanten van Plato."){:data-caption="De vierkanten van Plato." .dark-only width="30%"}


## Gevraagd
Schrijf een programma dat de oppervlakte van het grootste vierkant vraagt en vervolgens de zijden van de kleiner wordende vierkanten berekent. **Rond** telkens **af** op 2 cijfers na de komma.

#### Voorbeeld
Indien het grootste vierkant een oppervlakte van `144` m² heeft, dan verschijnt er
```
De lengte van de zijde van vierkant 1 is 12.0 m.
De oppervlakte van vierkant 2 is 36.0 m².
De lengte van de zijde van vierkant 2 is 6.0 m.
De oppervlakte van vierkant 3 is 9.0 m².
De lengte van de zijde van vierkant 3 is 3.0 m.
De oppervlakte van vierkant 4 is 2.25 m².
De lengte van de zijde van vierkant 4 is 1.5 m.
```

{: .callout.callout-info}
>#### Tips
> - Vergeet niet om de math module eerst te importeren met `import math`.
> - De lengte van de zijde van elk kleiner vierkant kan worden berekend door de **wortel** te nemen van de oppervlakte van het kleinere vierkant. 

