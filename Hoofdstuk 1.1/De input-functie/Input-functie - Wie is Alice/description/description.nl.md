## Doel

In deze oefening leer je een 
* variabele aanmaken;
* de `input()`-functie gebruiken;
* en de inhoud van de variabelen naar het scherm printen.

## Opgave

* Vraag de gebruiker om zijn/haar/hun naam in te voeren. Gebruik hiervoor de `input()`-functie;
* Sla de ingevoerde naam op in een variabele `naam`;
* Geef de tekst `"Hallo, mijn naam is"` en de inhoud van de variabele `bericht` weer op het scherm.


#### Voorbeeld 1

Bij deze invoer:
```
Voer je naam in: Alice
```

Verschijnt deze uitvoer:
```
Hallo, mijn naam is Alice
```

#### Voorbeeld 2

Bij deze invoer:
```
Voer je naam in: Voldemort
```

Verschijnt deze uitvoer:
```
Hallo, mijn naam is Voldemort
```


{: .callout.callout-info}
>#### Tip
>Een kommateken voegt **automatisch** een spatie toe binnen de `print()`-functie. We verduidelijken hieronder: 
> ```python
   print('Hallo, mijn naam is ', naam)
  ```
> Indien in de variabele `naam` dan `Robbe` opgeslagen werd, verschijnt er:
> ```
  Hallo, mijn naam is  Robbe
  ```
> Je merkt dat er een spatie **teveel** staat! Het **spatieteken** aan het einde van de eerste string, dus voor het sluiten van de aanhalingstekens, wordt hier gecombineerd met de **spatie** die ontstaat door het **kommateken**. 
