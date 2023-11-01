Tekstverwerkers hebben een algoritme nodig om een alinea's tekst op te splitsen in regels die een vooraf ingestelde maximale lengte niet overschrijden.

Er bestaan verschillende algoritmen om dit te realiseren en in het algemeen geven die aanleiding tot alinea's die er verschillend uitzien. Meestal wenst men een opsplitsing die niet al te "rafelig" is, d.w.z. dat alle regels zo goed als mogelijk de maximale lengte benutten. Een manier om de "rafeligheid" te kwantificeren is d.m.v. de som van de kwadraten van de verschillen tussen de maximaal toegelaten lengte en de effectieve lengte van de verschillende regels. In formulevorm wordt dit:

$$
\mathsf{ \sum_{i=1}^{\text{aantal regels}}( \text{maximale lengte} - \text{lengte regel }i)^2 }
$$

Een eenvoudig algoritme om een opsplitsing van een alinea te maken is het volgende: maak telkens regels die zo lang mogelijk zijn, d.w.z. dat wanneer een woord nog volledig op een regel past, dit woord dan op die regel geplaatst wordt. Het is pas wanneer een woord niet meer op de huidige regel past dat een nieuwe regel wordt begonnen. Omdat dit algoritme geen rekening houdt met de woorden die nog komen noemen we dit een gulzig algoritme.

Stel dat de tekst `Dit is een makkie` moet worden opgesplitst in regels waarvoor de maximale lengte gelijk is aan 7, dan levert het beschreven algoritme de volgende alinea:

```
----+--
Dit is
een
makkie
```

De rafeligheid van deze alinea is:

$$
\mathsf{(7 − 6)^2 + (7 − 3)^2 + (7 − 6)^2 = 1 + 16 + 1 = 18}
$$

## Opgave

Jouw taak is om voor een bepaalde tekst en maximale regellengte te berekenen wat de rafeligheid is van de alinea die wordt geproduceerd door het hierboven beschreven gulzige algoritme.

#### Voorbeelden
De eerste regel bevat het aantal testgevallen. Per testgeval volgen er twee regels. De eerste regel van elk testgeval bevat de maximale lengte van de regels in de alinea. De tweede regel van elk testgeval bevat de tekst die moet worden geformatteerd m.b.v. het gulzige algoritme. Deze tekst bestaat uit woorden die telkens van elkaar gescheiden worden door één enkele spatie.

Voor het eerste en na het laatste woord staan er geen spaties. We beloven dat geen enkel woord langer is dan de maximale regellengte, en dat de tekst steeds minstens één woord bevat.

```
3
7
Dit is een makkie
7
Perfect
10
Deze editie is de beste ooit
```

Per testgeval druk je  één regel af. Deze regel bevat twee getallen gescheiden door één spatie:

- Het eerste getal stelt de index van het testgeval voor. Het eerste testgeval heeft index 1.
- Het tweede getal is de berekende rafeligheidsscore.

```
1 18
2 0
3 77
```