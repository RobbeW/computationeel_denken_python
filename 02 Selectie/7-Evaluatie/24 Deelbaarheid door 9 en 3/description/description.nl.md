## Gegeven
Sommige getallen zijn snel te testen op deelbaarheid door **3 en deelbaarheid door 9.**

## Rekenregel
* Een getal is deelbaar door 3 als de som van zijn cijfers deelbaar is door 3.
* Een getal is deelbaar door 9 als de som van zijn cijfers deelbaar is door 9.
* Je werkt hier met een **natuurlijk getal van exact 4 cijfers.**

## Gevraagd
Schrijf een programma dat:
* een natuurlijk getal van 4 cijfers inleest,
* de 4 cijfers afzonderlijk bepaalt,
* de som van de cijfers berekent,
* en daarna print:
*       of het getal deelbaar is door 3 en 9,
*       of wel door 3 maar niet door 9,
*       of door geen van beide,
* en ook uitlegt waarom via de cijfersom (zoals in de voorbeelden).

## Voorbeelden
#### Invoer
```
1908
```

#### Uitvoer
```
Het getal is deelbaar door 3 en 9.
Dit kan je controleren door: 1, 9, 0 en 8 op te tellen, zo bekom je 18.
Deze som is deelbaar door 3 en 9.
```

#### Invoer
```
1302
```

#### Uitvoer
```
Het getal is deelbaar door 3 en niet door 9.
Dit kan je controleren door: 1, 3, 0 en 2 op te tellen, zo bekom je 6.
Deze som is deelbaar door 3.
```

#### Invoer
```
3401
```

#### Uitvoer
```
Het getal is niet deelbaar door 9 en 3.
Dit kan je controleren door: 3, 4, 0 en 1 op te tellen, zo bekom je 8.
Deze som is niet deelbaar door 9, noch door 3.
```