## Gegeven

Een koeriersbedrijf hanteert volgende regels voor het bepalen van de prijs van een pakje:

* `basisprijs`: 2.00 euro
* `massa`: extra per **begonnen** 20 gram: 0.40 euro
* `afstand`: extra per **begonnen** 10 km: 0.30 euro

## Gevraagd
* Schrijf een programma dat `vraagt` naar de massa van het pakje en de afstand (== `input-functie`);
* Bereken de prijs van het pakje volgens de gegeven formule;
* `Print` de prijs op het scherm met een verzorgde volzin.


## Invoer
```
Voer de massa van het pakje in (in gram): 68
Voer de afstand in (in km): 102
```
## Uitvoer
```
De prijs om het pakje te versturen is ... euro.
```

{: .callout.callout-success}
>## Tips
>* Start jouw algoritme met een `import math`.
>* Gebruik de `input()-functie` om de gebruiker naar de massa van het pakje en de afstand te vragen. 
>* Vergeet niet om de input om te zetten naar een `float` of `int`.
>* Bereken het aantal extra kosten voor de massa en de afstand met behulp van de formule en `math.ceil()`.
>* Bereken de totale prijs door de basisprijs op te tellen bij de extra kosten voor massa en afstand.
>* Rond de totaalprijs af naar een getal met twee decimalen. 
