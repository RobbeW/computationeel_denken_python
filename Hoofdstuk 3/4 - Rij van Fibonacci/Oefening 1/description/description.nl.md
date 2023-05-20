# Rij van Fibonacci

## Gegeven: 
* Sla de eerste 100 getallen van de rij van Fibonacci op in een lijst;
* Vraag daarna aan de gebruiker welk van de 100 getallen hij wil zien;
* Druk dat getal af.

De lijst van Fibonacci gaat als volgt:
```
1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...

```

Of in formulevorm: 
```
u(1) = 1

u(2) = 1

u(n) = u(n - 1) + u(n - 2)
```

## Gevraagd: 
* Schrijf een programma dat de eerste 100 getallen van de Fibonacci-reeks berekent en deze in een lijst opslaat;
* Vraag de gebruiker welk getal van de Fibonacci-reeks (tussen 1 en 100) hij wil zien;
* Print het gekozen getal van de Fibonacci-reeks op het scherm.

## Invoer: 
```
Voer het getal in van de Fibonacci-reeks dat u wilt zien (tussen 1 en 100): 13

```

## Uitvoer: 
```
Het 20e getal in de Fibonacci-reeks is ...
```

## Tips: 
* Gebruik een `lijst` om de eerste 100 getallen van de Fibonacci-reeks op te slaan;
* We laten die `lijst`starten als volgt: `fibonaci = [0, 1]`
* Gebruik een `for-lus` om de getallen van de Fibonacci-reeks te berekenen en aan de lijst toe te voegen;
* Gebruik hiervoor de `append-functie`;
* Gebruik de `input()-functie` om de gebruiker te vragen welk getal van de Fibonacci-reeks hij wil zien;
* Vergeet niet om de input om te zetten naar een int;
* Print het gekozen getal van de Fibonacci-reeks naar het scherm met behulp van de print()-functie;
* Vergeet niet om de index van de lijst met 1 te verminderen, omdat de indexen in Python vanaf 0 beginnen.
