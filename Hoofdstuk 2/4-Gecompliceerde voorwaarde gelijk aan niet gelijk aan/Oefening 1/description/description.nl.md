# Gecompliceerde Voorwaarde - Gelijk aan of niet gelijk aan - Oefening 1

## Gegeven: 
* Op een webshop krijg je de vraag op het einde of je een kortingscode hebt of niet. 
* Met de code **november10** krijg je 10% korting, met de code **Twitch20** 20%. 
* Je kan slechts één code ingeven.
* De standaard leveringskosten bedragen 4.80 euro. 

## Gevraagd: 
* Schrijf een programma dat vraagt naar het bestelde bedrag en een eventuele kortingscode (== input-functie);
* Bereken de korting op basis van de ingevoerde kortingscode;
* Voeg de leveringskosten toe aan het bedrag;
* Print het te betalen bedrag op het scherm.
* Rond het bedrag af tot twee decimalen.

## Invoer: 
```
Voer het bestelde bedrag in: 50.00
Voer de kortingscode in (indien van toepassing): Twitch20
```

## Uitvoer: 
```
Het te betalen bedrag is ... euro.
```

## Tips:  
* Gebruik de `input()-functie` om de gebruiker naar het bestelde bedrag en de kortingscode te vragen;
* Vergeet niet om het datatype om te zetten naar een `float` of `int` indien nodig; 
* Gebruik voorwaardelijke uitspraken (`if`, `elif`, `else`) om te bepalen welke korting hoort bij de ingevoerde kortingscode;
* Bereken het te betalen bedrag door de korting toe te passen en de leveringskosten toe te voegen;
* Print het te betalen bedrag, afgerond tot twee decimalen, naar het scherm met behulp van de `print()-functie`.
