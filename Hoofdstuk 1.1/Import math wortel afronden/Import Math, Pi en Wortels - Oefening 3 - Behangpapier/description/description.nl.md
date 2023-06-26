## Gegeven: 

Om te berekenen hoeveel rollen behangpapier er nodig zijn om een muur te behangen, moet je de `lengte` en de `hoogte` van de muur weten en de afmetingen van het behangpapier. 
Eén rol behangpapier is `10 meter lang` en `52 cm breed`.

## Gevraagd: 
* Schrijf een programma dat `vraagt` naar de `lengte` en `hoogte` van de muur (== `input-functie`);
* Bereken het aantal rollen behangpapier dat nodig is om de muur te behangen;
* `Print` het aantal benodigde rollen behangpapier op het scherm.

## Invoer: 
```
Voer de lengte van de muur in (in meter): 20
Voer de hoogte van de muur in (in meter): 2.8
```

## Uitvoer: 
```
Het aantal benodigde rollen behangpapier is ... rollen.
```

{: .callout.callout-success}
>## Tips: 
>* Start jouw algoritme met `import math`. 
>* Gebruik de `input()-functie` om de gebruiker naar de lengte en hoogte van de muur te vragen. 
>* Vergeet niet om de `input` om te zetten naar een `float` of `int`.
>* Bereken het `oppervlak van de muur` met de formule: `oppervlak_muur = lengte * hoogte`.
>* Bereken het `oppervlak van één rol behangpapier` met de formule: `oppervlak_behangpapier = 10 * (52 / 100)`. (Let op: de breedte moet in meters worden omgezet).
>* Bereken het aantal benodigde rollen behangpapier door het **oppervlak van de muur te delen door het oppervlak van één rol behangpapier** en **rond dit getal naar boven af** met behulp van `math.ceil()`.
>* Print het berekende aantal benodigde rollen behangpapier op het scherm met behulp van de `print()-functie`.