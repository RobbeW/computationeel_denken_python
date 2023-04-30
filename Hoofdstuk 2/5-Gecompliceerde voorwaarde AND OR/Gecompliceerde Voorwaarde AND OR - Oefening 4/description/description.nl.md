# Gecompliceerde Voorwaarde AND OR - Oefening 4

## Gegeven: 
Er zijn 3 toetsen, elk op 20 punten.
Je bent pas geslaagd wanneer je de helft of meer scoort op **elke** toets.
Je krijgt de titel **onderscheiding** wanneer jouw `percentage` hoger is dan 67%. 

## Gevraagd:
* Schrijf een programma dat vraagt naar de scores van de 3 toetsen (== input-functie);
* Bereken het percentage van de totale score;
* Druk het percentage af;
* Print de beoordeling op basis van het behaalde percentage: 'onderscheiding', 'geslaagd' of 'niet geslaagd'.

## Invoer:
```
Voer de score van toets 1 in: 15
Voer de score van toets 2 in: 12
Voer de score van toets 3 in: 18

```

## Uitvoer: 
```
Je hebt 75% behaald.
Beoordeling: onderscheiding.

```

## Tips: 
* Gebruik de `input()-functie` om de gebruiker naar de scores van de 3 toetsen te vragen. 
* Vergeet niet om de `input` om te zetten naar een int.
* Bereken het `percentage` van de totale score door de som van de scores te delen door het totale aantal punten (60) en te vermenigvuldigen met 100.
* Gebruik voorwaardelijke uitspraken (`if`, `elif`, `else`) om te bepalen welke beoordeling hoort bij het behaalde `percentage`.
* Print het `percentage` en de `beoordeling` naar het scherm met behulp van de `print()-functie`.