Wanneer ik aardappelen kook wil ik graag dat de stukken aardappel ongeveer even snel gaar zijn: ik wil geen halfgare en overgare aardappelen op mijn bord. Daarom snijd ik die aardappelen in stukken tot de stukken hoogstens een vooraf bepaalde grootheid G verschillen. Ik heb namelijk een systeem uitgedokterd om aan aardappelen een grootte toe te kennen en dat is altijd een geheel getal. Dat maakt het vergelijken van die aardappelen gemakkelijk en ook de procedure om een aardappel (of een stuk aardappel) in twee stukken te snijden: als de grootte even is, dan snijd ik in twee gelijke delen.

Als de grootte oneven is, dan snijd ik in twee delen die juist  één grootheidverschillen. Dus, een (stuk) aardappel van grootte 8 snijd ik (als het nodig is) in twee stukken van 4. Een (stuk) aardappel van grootte 9 snijd ik in een stuk van 4 en eentje van 5. Gegeven de grootte van de initiële aardappelen, en G, hoeveel keer moet ik een (stuk) aardappel doorsnijden?

## Opgave
Je krijgt als invoer de grootte van elke aardappel en de G, het maximale verschil tussen twee stukken aardappel op het einde. Je programma geeft als resultaat het minimaal aantal keer dat ik een (stuk) aardappel doorsnijd zodat het verschil in grootte tussen twee stukken niet groter is dan G.

#### Voorbeeld

De eerste regel stelt het aantal testgevallen voor. Per testgeval volgt één regel met daarop enkel gehele getallen > 0 gescheiden door een blanco:

- G; 1 ≤ G ≤ 10
- A het aantal aardappelen; 1 ≤ A ≤ 100
- A getallen die de groottes van de aardappelen voorstellen; groottes zijn kleiner dan 101

```
3
1 3 2 4 7
2 3 4 8 14
1 4 5 7 11 13
```

Per testgeval druk je één regel af: die begint met het volgnummer van het testgeval. Dan komt het aantal keer dat een (stuk) aardappel moet doorgesneden worden. Die twee getallen worden gescheiden door één blanco.

```
1 3
2 4
3 10
```