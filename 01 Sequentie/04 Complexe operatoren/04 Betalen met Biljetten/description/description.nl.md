## Gegeven

Bij het betalen van een bedrag in euro's, kunnen verschillende soorten biljetten en munten worden gebruikt. Om het **minimale aantal** biljetten en munten te bepalen dat nodig is om een bepaald bedrag te betalen, moet je het bedrag eerst opdelen in biljetten en munten van verschillende waardes.

![Verschillende euro biljetten.](media/markus-spiske.jpg "Foto door Markus Spiske op Unsplash."){:data-caption="Verschillende euro biljetten." width="35%"}

Het minimale **aantal biljetten** van € 50 dat nodig is om het bedrag te betalen kunnen we achterhalen met volgende code:

```python
bedrag = int( input( "Voer het te betalen bedrag in euro's in: " ) )

aantal_vijftig = bedrag // 50 # dit berekent het quotiënt zonder rest. 
restbedrag = bedrag % 50      # dit berekent de rest zonder quotiënt en kent deze toe aan de variabele restbedrag. 
                              # vervolgens kan je verder werken met dit restbedrag
```

## Gevraagd

* Gebruik bovenstaande code als **basis en breid deze uit** met het bepalen van het aantal biljetten van `20`, `10` en `5 euro`, en het aantal munten van `2 euro` en `1 euro` dat nodig is om het bedrag te betalen. Gebruik gelijkaardige notatie als in de bovenstaande code voor het bepalen van het aantal biljetten en munten.

* Print het totale aantal biljetten en munten dat nodig is om het bedrag te betalen. 

#### Voorbeeld

Bij een invoer van € 2 543 verschijnt er:

```
biljet 50: 50
biljet 20: 2
biljet 10: 0
biljet 5: 0
munt 2: 1
munt 1: 1
```

{: .callout.callout-info}
>#### Tips
> - Voer tests uit met verschillende bedragen, zoals € 100, € 73, € 37, enzovoort. Zorg ervoor dat de code correct werkt en het juiste aantal biljetten en munten weergeeft.
> - Vergeet niet om te **debuggen** en eventuele fouten op te lossen.

