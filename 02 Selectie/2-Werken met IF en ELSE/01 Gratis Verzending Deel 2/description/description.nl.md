## Gegeven
Gratis verzending is beschikbaar **als** het `aankoopbedrag` gelijk is aan, of hoger is dan, 20 euro. 
**Anders** kost de verzending 4 euro.

## Gevraagd
* Schrijf een programma dat vraagt naar het `aankoopbedrag` bij de webshop;
* Bepaal of de gebruiker gratis verzending krijgt;
* **Als** de gebruiker in aanmerking komt voor gratis verzending, toon dan een boodschap en het `totaalbedrag` op het scherm;
* **Anders** komt de gebruiker niet in aanmerking voor gratis verzending. Bereken dan het totale bedrag en geef dit weer op het scherm.

#### Voorbeeld 1
```
Voer het aankoopbedrag in: 18.00
```
Leidt tot de uitvoer
```
Je komt niet in aanmerking voor gratis verzending.
Het totaalbedrag inclusief verzending is 22.0 euro.
```

#### Voorbeeld 2
```
Voer het aankoopbedrag in: 21.00
```
Leidt tot de uitvoer
```
Je komt in aanmerking voor gratis verzending.
Het totaalbedrag inclusief verzending is 21.0 euro.
```

{: .callout.callout-info}
>#### Tips
>- Gebruik een `if`-statement om te controleren of het aankoopbedrag gelijk is aan, of hoger is dan, 20 euro.
>- Als het `aankoopbedrag` niet voldoet aan de voorwaarde, bereken het bedrag plus verzending en gebruik de `print()`-functie om dit naar het scherm te sturen in een volzin met een onderwerp, hoofdletters, leestekens, enz.
