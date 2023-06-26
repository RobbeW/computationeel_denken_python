## Gegeven: 
Een positief geheel getal. 


## Gevraagd: 
* Vraag de gebruiker om een positief geheel getal in te voeren.
* Voor elke mogelijke deler van dit getal (van 1 tot het getal zelf), bereken het quotiënt van het getal gedeeld door de deler.
* Controleer of dit quotiënt een positief geheel getal is (d.w.z., de rest na deling is nul) en dus geen decimaal getal.
* `Als` dat zo is, voeg die deler toe aan een `lijst`. 

## Invoer: 
```
Voer een positief geheel getal in: 25

```

## Uitvoer: 
```
De delers van 25 die een positief geheel getal als quotiënt uitkomen zijn: [...] 


```
{: .callout.callout-success}
>## Tips: 
>* Gebruik de `input()-functie` om de gebruiker om een getal te vragen. 
>* Vergeet niet om de input om te zetten naar een `int`.
>* Gebruik een `while-lus` om door elk mogelijk deler van het getal te itereren.
>* Gebruik de `modulo-operator %` om de rest na deling te berekenen. 
>* Als het `getal % de deler` gelijk is aan nul, dan is het quotiënt een positief geheel getal.
>* Voeg die deler dan toe aan een `lijst` via de `lijst.append-functie`. 
