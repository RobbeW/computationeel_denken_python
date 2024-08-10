## Gegeven

Yulia nam het volgende datatarief met een bepaalde datalimiet x bij haar internetprovider. Elke megabyte die ze niet gebruikt in de maand wordt overgdragen naar de volgende maand en kan dan gebruikt worden. Natuurlijk kan ze enkel de megabytes gebruiken die ze nog ter beschikking heeft.

As we weten hoeveel megabytes Yulia in de voorbije n maanden gebruikt heeft, bereken dan **hoeveel data** ze kan gebruiken de **volgende maand**.

## Gevraagd

- Schrijf een programma dat eerst de datalimiet `x` opvraagt, daarna wordt gevraagd hoeveel maanden er al gepasseerd zijn.
- Voor elke maand wordt vervolgens het gebruik aan de gebruiker gevraagd. 
- Tot slot berekent het programma de datalimiet voor de volgende maand. 

#### Voorbeelden

Stel dat er een (zeer beperkte) datalimiet van `10` MB per maand is. Yulia is reeds `3` maanden bij haar internetprovider. Ze geeft hierna achtereenvolgend de verbruiken `4`, `6` en `2` MB in. Er verschijnt nu:

```
Beschikbaar: 28 MB
```

Stel dat er een (zeer beperkte) datalimiet van `10` MB per maand is. Yulia is reeds `3` maanden bij haar internetprovider. Ze geeft hierna achtereenvolgend de verbruiken `10`, `2` en `12` MB in. De derde maand kon ze 12 MB gebruiken want de voorbije maand had ze namelijk 8 MB opgespaard. Er verschijnt nu:

```
Beschikbaar: 16 MB
```

Stel dat er een (zeer beperkte) datalimiet van `15` MB per maand is. Yulia is reeds `3` maanden bij haar internetprovider. Ze geeft hierna achtereenvolgend de verbruiken `15`, `10` en `20` MB in. Er verschijnt nu:

```
Beschikbaar: 15 MB
```

{: .callout.callout-secondary}
>#### Bron
> COCI 2016/2017, Kroatië.