## Gegeven

Een computer leest de antwoorden van een leerling op een tien problemen in als `"JJFFJFFJJJ"`. Een `"J"` staat voor een juist en `"F"` voor een foutief antwoord. De score op een probleem hangt af van het score op het vorige probleem (indien het ook juist was).

Zo is de score op het tiende probleem in dit voorbeeld 3, doordat het de derde opeenvolgende juiste oplossing was. De volledige score van dit voorbeeld kan je dus als volgt berekenen: 1 + 2 + 0 + 0 + 1 + 0 + 0 + 1 + 2 + 3 = 10.

## Gevraagd
Schrijf een programma dat zo'n tekstregel omzet in een score. Vraag aan de gebruiker eerst de tekstregel en geef nadien de score weer.

#### Voorbeelden

Bij de antwoorden `"JJFFJFFJJJ"` verschijnt als score:
```
10
```

Bij de antwoorden `"JJFFJJFFFJJ"` verschijnt als score:
```
9
```

Bij de antwoorden `"JFJFJFJFJFJFJF"` verschijnt als score:
```
7
```

Bij de antwoorden `"JJJJJJJJJJ"` verschijnt als score:
```
55
```

Bij de antwoorden `"JJJJFJJJJFJJJJF"` verschijnt als score:
```
30
```

{: .callout.callout-secondary}
>#### Bron
> Universiteit van Valladolid (UVa), probleem *Score*.

