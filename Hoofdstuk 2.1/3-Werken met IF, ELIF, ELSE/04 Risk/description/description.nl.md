## Gegeven

<a href="https://nl.wikipedia.org/wiki/Risk_(bordspel)">Risk</a> is een klassiek bordspel waarbij het (meestal) de bedoeling is dat je de ganse wereldkaart gaat veroveren. Elk gebied dat je bezet geeft je per beurt een aantal legers die je kan gebruiken om een tegenstander aan te vallen.

![Een spelletje Risk.](media/dave-photoz.jpg "Foto door Dave Photoz op Unsplash."){:data-caption="Een spelletje Risk." width="40%"}

Bij het aanvallen is het steeds zo dat de aanvaller met drie dobbelstenen gooit en de verdediger met slechts twee dobbelstenen mag gooien. Daarna wordt het aantal ogen gerangschikt van hoog naar laag en als de aanvaller bij zijn twee hoogste waarden telkens **hoger scoort** dan de twee hoogste waarden van de verdediger, dan worden twee legereenheden van de verdediger vernietigd.

Een voorbeeld ter verduidelijking.

Als de **aanvaller** de volgende dobbelstenen gooit:

 <span class="mdi mdi-36px mdi-dice-2-outline"></span> <span class="mdi mdi-36px mdi-dice-5-outline"></span> <span class="mdi mdi-36px mdi-dice-1-outline"></span>
 
en de **verdediger** gooit op zijn beurt:

 <span class="mdi mdi-36px mdi-dice-4-outline"></span> <span class="mdi mdi-36px mdi-dice-3-outline"></span>

In dit geval verliezen beide legers een eenheid. De 5 van de aanvaller wint immers van de 4 van de verdediging. Maar de volgende hoogste waarde van de aanvaller, namelijk een 2, verlies van de volgende hoogste waarde van de verdediging, namelijk een 3.

## Gevraagd

Schrijf een programma waarbij de aanvaller de eerste drie worpen dient in te geven en daarna de verdediging de volgende twee worpen intikt. Je programma geeft vervolgens weer hoeveel legereenheden elk verliest.

#### Voorbeeld 1

In het vorige voorbeeld tikt de aanvaller achtereenvolgend `2`, `5` en `1` in. De verdediger tikt `4` en `3` in. Er verschijnt:

```
Verloren eenheden aanvaller: 1
Verloren eenheden verdediging: 1
```


#### Voorbeeld 2

Stelt dat de **aanvaller** de volgende dobbelstenen gooit:

<span class="mdi mdi-36px mdi-dice-4-outline"></span> <span class="mdi mdi-36px mdi-dice-5-outline"></span> <span class="mdi mdi-36px mdi-dice-4-outline"></span>
 
en de **verdediger** gooit op zijn beurt:

 <span class="mdi mdi-36px mdi-dice-5-outline"></span> <span class="mdi mdi-36px mdi-dice-4-outline"></span>

dan verlies de aanvaller twee legereenheden! De grootste worpen moeten immers **meer** zijn dan die van de verdediging.

In dit geval tikt de aanvaller in `4`, `5` en `4` in. De verdediger tikt `5` en `4` in. Er verschijnt:

```
Verloren eenheden aanvaller: 2
Verloren eenheden verdediging: 0
```
