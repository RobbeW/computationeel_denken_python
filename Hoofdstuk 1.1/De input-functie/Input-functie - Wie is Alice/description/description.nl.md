## Doel

In deze oefening leer je een 
* variabele aanmaken;
* een string aan de variabele toevoegen;
* de `input()`-functie gebruiken;
* en de inhoud van de variabelen naar het scherm printen.

## Opgave

* Maak een variabele met de naam `bericht` en wijs er de string `"Hallo, mijn naam is"` aan toe;
* Vraag de gebruiker om zijn/haar/hun naam in te voeren. Gebruik hiervoor de `input()`-functie;
* Voeg de ingevoerde naam toe aan de variabele `bericht`;
* Print de inhoud van de variabele `bericht` naar het scherm.

## Invoer
```
Alice
```

## Uitvoer
```
Voer je naam in: Alice
Hallo, mijn naam is Alice
```

## Tip!
Een kommateken voegt **automatisch** een spatie toe binnen de `print()`-functie. We verduidelijken hieronder: 
```python
print('Hallo, mijn naam is ', variabele_naam)
```

Indien in `variabele_naam` dan `Robbe` opgeslagen werd, verschijnt er:
```
Hallo, mijn naam is  Robbe
```

Je merkt dat er een spatie **teveel** staat! Het **spatieteken** aan het einde van de eerste string, dus voor het sluiten van de aanhalingstekens, wordt hier gecombineerd met de **spatie** die ontstaat door het **kommateken**. 
