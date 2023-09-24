## Gegeven

Om te berekenen hoeveel rollen behangpapier er nodig zijn om een muur te behangen, moet je de `lengte` en de `hoogte` van de muur weten en de afmetingen van het behangpapier. Een rol behangpapier is meestal 10 meter lang en 52 cm breed.

![Een rol behangpapier.](media/Behangpapier.png "Een rol behangpapier."){:data-caption="Een rol behangpapier" .light-only width="293px"}

## Gevraagd

- Schrijf een programma dat **vraagt** naar de lengte en hoogte van de muur;
- Bereken het aantal rollen behangpapier dat nodig is om de muur te behangen;
- Geef dit aantal rollen weer op het scherm.

## Invoer
Hieronder zie je een mogelijk voorbeeld:
```
Voer de lengte van de muur in (in meter): 20
Voer de hoogte van de muur in (in meter): 2.8
```

## Uitvoer

```
Het aantal benodigde rollen behangpapier is ... rollen.
```

{: .callout.callout-info}
>#### Tips
> - Vergeet niet om de `input` om te zetten naar een `float` of `int`.
> - Bereken de oppervlak van één rol behangpapier. (**Let op**: de breedte moet in meters worden omgezet).
> - Bereken het aantal benodigde rollen behangpapier door de oppervlakte van de muur te delen door de oppervlakte van één rol behangpapier en **rond dit getal naar boven af** met behulp van `math.ceil()`. (Importeer dus ook de bibliotheek `math`)
