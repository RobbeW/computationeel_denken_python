# Werken met IF, ELIF en ELSE - Oefening 1

## Gegeven: 
* Gratis verzending voor `aankoopbedragen` van 20 euro of meer.
* Verzendkosten van 4 euro voor `aankoopbedragen` lager dan 20 euro.
* 10% korting voor `aankoopbedragen` van 100 euro of meer.

## Gevraagd: 
* Lees het bestelde `bedrag` in.
* Bepaal of de gebruiker 10% korting krijgt en bereken het `totaalbedrag` na de korting, indien van toepassing.
* Bepaal of de gebruiker gratis verzending krijgt en bereken het `totaalbedrag` na verzendkosten, indien van toepassing.
* Druk het `totaalbedrag` en de eventuele kortingen en verzendkosten af in een volzin.

## Invoer: 
```
Voer het bestelde bedrag in: 113.89
```

## Uitvoer: 
```
Je krijgt 10% korting.
Je krijgt gratis verzending.
Het totaalbedrag is 102.50 euro.
```

## Tips: 
* Gebruik de `input()-functie` om de gebruiker naar het bestelde bedrag te vragen. 
* Vergeet niet om de invoer om te zetten naar een `float` of `int`.
* Gebruik `if-statements` om te controleren of de gebruiker korting en/of gratis verzending krijgt.
* Bereken het `totaalbedrag` op basis van de korting en verzendkosten.
* Gebruik de `print()-functie` om het `totaalbedrag` en de eventuele kortingen en verzendkosten naar het scherm te sturen. 
* Vergeet niet om volzinnen te gebruiken.
* **Rond** het `eindbedrag` **af** naar een getal met twee decimalen. 