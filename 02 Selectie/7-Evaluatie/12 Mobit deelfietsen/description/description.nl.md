## Gegeven

<a href="https://www.mobit.eu" target="_blank">Mobit</a> is een aanbieder van deelfietsen. Via een app kan je een fiets ontgrendelen en na het gebruik wordt het verontschuldigde bedrag automatisch berekend. 

![Let's Mobit.](media/mobit.jpg "Let's Mobit."){:data-caption="Let's Mobit." width="35%"}

Men hanteert hierbij de volgende tariefkaart, waarbij er telkens per **begonnen** blok van 20 minuten wordt gerekend.

| Periode       | Prijs per blok  |
|:--------------|:---------------:|
| 1ste uur      | € 0,45          |
| 2de uur       | € 0,65          |
| 3de uur       | € 0,80          |
| Volgende uren | € 1,00          |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

Een **uitzondering** hierop zijn zeer korte ritten van minder dan 4 minuten die slechts € 0,29 kosten

## Gevraagd

Schrijf een programma dat naar de fietstijd (in minuten) vraagt en vervolgens het verontschuldigde bedrag weergeeft. **Rond af** op twee decimalen.

#### Voorbeelden
Als een peroon `35` minuten fietste dan worden er twee blokken aangerekend. Beide blokken zitten in de eerste categorie, de kostprijs is dus € 0,90. Er verschijnt:

```
Kostprijs: € 0.9
```

Als een persoon de fiets gedurende 1 uur en 12 minuten (of dus `72` minuten) nodig had, dan verschijnt er:

```
Kostprijs: € 2.0
```

Er worden immers vier blokken aangerekend, de eerste drie blokken behoren tot de eerste categorie, het volgende blok kostte € 0,65. 


