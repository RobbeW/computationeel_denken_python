# Complexe Operatoren - Oefening 3

## Gegeven:

Bij het betalen van een bedrag in euro's, kunnen verschillende soorten biljetten en munten worden gebruikt. Om het aantal biljetten en munten te bepalen dat nodig is om een bepaald bedrag te betalen, moet je het bedrag eerst opdelen in biljetten en munten van verschillende waardes.


Het `aantal biljetten` van 50 euro dat nodig is om het bedrag te betalen kunnen we achterhalen met volgende code:

```
bedrag = int(input("Voer het te betalen bedrag in euro's in: "))

aantal_vijftig = bedrag // 50 # dit berekent het quotiënt zonder rest. 
bedrag %= 50                  # dit berekent bepaalt de rest zonder quotiënt en kent deze toe aan de variabele bedrag. 
                              # met de rest gaan we verder om te berekenen hoeveel briefjes van ... we nodig hebben. 
```

## Gevraagd: 

* Gebruik bovenstaande code als **basis en breid deze uit** met het bepalen van het aantal biljetten van `20`, `10` en `5 euro`, en het aantal munten van `2 euro` en `1 euro` dat nodig is om het bedrag te betalen. Gebruik dezelfde notatie als in de bovenstaande code voor het bepalen van het aantal biljetten en munten.

* Print het totale aantal biljetten en munten dat nodig is om het bedrag van `2543 euro` te betalen. 

## Invoer: 
```
Voer het bedrag in: 2543
```


## Uitvoer: 
```
U hebt  ...  biljetten van 50 euro,  ...  biljetten van 20 euro,  ...  biljetten van 10 euro, ...  biljetten van 5 euro,  ...  munten van 2 euro en  ...  munten van 1 euro nodig om het bedrag van  ... euro te betalen.

```


## Tips: 

* Voer tests uit met verschillende bedragen, zoals 100 euro, 73 euro, 37 euro, enzovoort. Zorg ervoor dat de code correct werkt en het juiste aantal biljetten en munten weergeeft.

* Vergeet niet om te **debuggen** en eventuele fouten op te lossen.

