# Het vermoeden van Collatz

## Gegeven: 
Het vermoeden van Collatz is een vermoeden in de getaltheorie dat zegt dat een bepaalde iteratie (=herhaling) in alle gevallen uitloopt op het getal 1, om het even welk getal n als beginwaarde gekozen wordt.

## Gevraagd: 
* Neem een **geheel getal n** als `beginwaarde`;
* Bereken een volgend getal met onderstaande regels:
* `Als n even is, dan deel je het door 2 (=n/2)`
* `Anders, als n oneven is, vermenigvuldig het met 3 en tel er 1 bij op (=n*3+1)`
* We **itereren of herhalen** deze bewerkingen **zolang** `n != 1`;
* Bij elke herhaling, `printen` telkens dit getal op het scherm;
* Bij het einde van onze oefeningen **printen** we **"Stop!"**. 

## Invoer: 

```
Voer een geheel getal in: 327

```

## Uitvoer: 
``` 
982
491.0
1474.0
... 
1.0
Stop!

``` 

## Tips:
* Gebruik de `% modulo`om te bepalen of `n`een even getal is; 
* Bij het opstellen van een voorwaarde, let op dat je dubbele gelijkheidstekens `==`gebruikt. 