## Gegeven

De <a href="https://nl.wikipedia.org/wiki/Driehoek_van_Sierpi%C5%84ski" target="_blank">driehoek van Sierpiński</a> is een <a href="https://nl.wikipedia.org/wiki/Fractal" target = "_blank">fractaal</a> gevonden door de Poolse wiskundige <a href="https://nl.wikipedia.org/wiki/Wac%C5%82aw_Sierpi%C5%84ski" target="_blank">Wacław Sierpiński</a>.

De driehoek ontstaat door te starten van een gelijkzijdige driehoek. Vervolgens wordt de driehoek gevormd door de middens van de zijden verwijderd. Dit proces wordt daarna opnieuw uitgevoerd voor elke nieuwe gelijkzijdige driehoek.

![Vorming van de driehoek van Sierpiński.](media/image.png "Vorming van de driehoek van Sierpiński."){:data-caption="Vorming van de driehoek van Sierpiński." .light-only width="236px"}

![Vorming van de driehoek van Sierpiński.](media/image_dark.png "Vorming van de driehoek van Sierpiński."){:data-caption="Vorming van de driehoek van Sierpiński." .dark-only width="236px"}

## Gevraagd
Schrijf een programma dat de oppervlakte van de oorspronkelijke driehoek vraagt en nadien het nummer in de iteratie. Vervolgens geef je telkens het aantal driehoeken weer en de resterende oppervlakte.

**Rond** bij de oppervlakte bij het afdrukken telkens **af** op 2 cijfers na de komma.

#### Voorbeeld
Stel dat de oorspronklijke oppervlakte 4 cm² bedraagt en het proces `5` keer wil herhalen, dan verschijnt er:
```
De startoppervlakte was 4.0 cm².
Na iteratie 1 zijn er 3 driehoeken en resteert er 3.0 cm².
Na iteratie 2 zijn er 9 driehoeken en resteert er 2.25 cm².
Na iteratie 3 zijn er 27 driehoeken en resteert er 1.69 cm².
Na iteratie 4 zijn er 81 driehoeken en resteert er 1.27 cm².
Na iteratie 5 zijn er 243 driehoeken en resteert er 0.95 cm².
```
