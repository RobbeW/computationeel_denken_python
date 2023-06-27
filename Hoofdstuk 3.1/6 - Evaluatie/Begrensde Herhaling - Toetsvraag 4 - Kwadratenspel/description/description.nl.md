## Gegeven
Het kwadraat van een getal is het product van dat getal met zichzelf. 
Bijvoorbeeld, het kwadraat van 4 is 16, omdat 4*4 = 16.

## Gevraagd

* Schrijf een programma dat een willekeurig getal van 1 tot en met 10 genereert;
* Print het getal naar het scherm;
* Het programma vraagt vervolgens aan de gebruiker wat hij/zij/hun denkt dat het kwadraat van dat getal is;
* Als het antwoord van de gebruiker correct is, print het programma "goed zo" en krijgt de gebruiker een punt;
* Als het antwoord onjuist is, print het programma de juiste oplossing in een nette zin op het scherm;
* Het programma moet 10 oefeningen stellen en aan het einde de totaalscore printen.

## Invoer (voorbeeld)

```
Wat is het kwadraat van 3? 9
Wat is het kwadraat van 7? 50
Wat is het kwadraat van 1? 1

```

## Uitvoer

```
Goed zo!
Fout, het juiste antwoord is 49.
Goed zo!
...
Je totaalscore is: 7/10.

```

{: .callout.callout-success}
>## Tips
>* Gebruik de `random.randint(1, 10)-functie` om een willekeurig getal tussen 1 en 10 te genereren.
>* Gebruik de `input()-functie` om de gebruiker om het kwadraat van het getal te vragen.
>* Vergeet niet om de invoer van de gebruiker naar een `int` om te zetten met de `int()-functie` voordat je het vergelijkt met het echte kwadraat.
>* Gebruik een `teller` om bij te houden hoeveel vragen de gebruiker correct heeft beantwoord.
>* Gebruik de `print()-functie` om de score van de gebruiker aan het einde van het programma te tonen.
