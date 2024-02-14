## Gevraagd
- Schrijf een programma dat twee getallen genereert tussen 1 en 10. 
- Vervolgens vraagt het programma aan de gebruiker om het `product` van deze twee getallen te berekenen.
- Is het antwoord **juist**, dan verschijnt de boodschap `"Goed zo!"` en krijgt de gebruiker een punt. Anders toont het programma de juiste oplossing.
- Het programma moet in totaal **vijf van deze opgaven** opstellen en aan het einde de totaalscore tonen.

#### Voorbeeld

Stel dat het programma de getallen `10` en `3` **willekeurig** aanmaakt.

```
Getal 1: 10
Getal 2: 3
```

De gebruiker tikt nu foutief `31` in als product. Er verschijnt:
```
Dat is niet correct. Het juiste antwoord is 30
```

De tweede keer maakt de computer willekeurig de getallen `2` en `7` aan.

```
Getal 1: 2
Getal 2: 7
```

De gebruiker tikt nu correct `14` in als product. Er verschijnt:
```
Goed zo!
```

En zo herhaalt zich dit totdat het programma op het einde weergeeft:

```
Je totaalscore is 2 op 5.
```


{: .callout.callout-info}
>#### Tips
>- Gebruik een lus om het programma 10 keer te laten herhalen. 
>- Houd de score bij in een variabele die je telkens met 1 verhoogt als het antwoord van de gebruiker juist is.
