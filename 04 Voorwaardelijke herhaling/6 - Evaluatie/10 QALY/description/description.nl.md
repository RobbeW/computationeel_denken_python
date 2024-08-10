## Gegeven

De <a href="https://nl.wikipedia.org/wiki/Quality-adjusted_life_year" target="_blank">Quality-Adjusted Life-Year</a> (QALY) of *extra levensjaar in goede gezondheid* is een manier om de levenskwaliteit van een persoon in een getal uit te drukken. In dit cijfer zit zowel de kwaliteit als de kwantiteit van het leven bevat. Dit cijfer wordt bijvoorbeeld door overheden gebruikt om financiëring van de zorgsector te onderzoeken.

De **kwaliteit** wordt beoordeeld met een getal tussen 0 en 1. Als iemand in perfect gezondheid leeft, dan is dit cijfer 1. Is iemand dood, dan is het cijfer 0. De kwaliteit kan bijvoorbeeld stijgen door een medische behandeling of dalen door ziekte.

![Een kwaliteitsvolle zonsondergang.](media/austin-schmid.jpg "Een kwaliteitsvolle zonsondergang."){:data-caption="Foto door Austin Schmid op Unsplash." width="35%"}

De QALY voor elke levensfase waar deze constant is kan men berekenen als *de kwaliteit vermenigvuldigt* met de *lengte van die periode* (in jaren uitgedrukt). Het doel van deze oefening is de **totale QALY** te gaan berekenen voor een persoon bij sterfte, indien de volledige geschiedenis gekend is.

## Gevraagd

- Schrijf een programma dat aan de gebruiker eerst het aantal periodes vraagt,
- Daar vraagt het programma **voor elke periode** in volgorde naar het aantal jaren (dit kan een kommagetal zijn) uit deze periode en nadien de kwaliteit (uitgedrukt als een cijfer tussen 0 en 1).

Uiteindelijk toon je de uiteindelijke leetijd en de totale QALY, afgerond op 3 decimalen.

#### Voorbeeld

Stel dat een persoon bij zijn overlijden `5` periodes of levensfasen gekend heeft.

1. De eerste levensfase duurde `12.0` jaar. De kwaliteit werd als `1.0` beoordeeld,
2. De volgende fase duurde `5.2` jaar, en door een ziekte daalde de kwaliteit naar `0.7`,
3. Na een behandeling duurde de volgende fase `10.7` jaar met een kwaliteit van `0.9`,
4. Het ging hierna opnieuw minder goed met de persoon, gedurende `20.4` jaar daalde de kwaliteit naar `0.5`,
5. De laatste fase duurde nog `30.0` jaar, maar de kwaliteit zakte verder naar `0.2`.

```
Deze persoon van 78.3 jaar had een totale QALY van 41.470
```

{: .callout.callout-secondary}
>#### Bron
> Rocky Mountain Regional Programming Contest 2018