## Gegeven
Er bestaan verschillende manieren om de grootte van een hoek uit te drukken. Wij gebruiken meestal het zestigtallige talstelsel om een hoek aan te duiden. En hoek wordt hierbij opgebouwd uit graden °, daarna minuten ' en seconden ''. Waarbij elke graad uit 60 minuten bestaat en elke minuut uit 60 seconden.

Een voorbeeld van een hoek in het zestigtallige stelsel is, 45° 28' 30", oftewel, 45 graden, 28 minuten en 30 seconden.

Je rekentoestel zal een hoek meestal in decimale graden uitdrukken, de vorige hoek wordt dan uitgedrukt als 45,475°. Dit komt ook perfect overeen want dit zou betekenen dat de hoek ongeveer 45,5° groot is. Je kan dit lezen als 45° en een halve graad, een halve graad is 30' wat inderdaad ongeveer overeen komt 28' 30".

## Gevraagd
Schrijf een programma dat een decimale hoek, als een *kommagetal*, vraagt en vervolgens berekent met welke hoek uit het zestigtallige talstelsel dit overeen komt.

#### Voorbeelden
Geeft men de hoek `45.475` in, dan verschijnt er:
```
Dit komt overeen met 45 graden 28 minuten en 30 seconden.
```

Geeft men de hoek `61.5` in, dan verschijnt er:
```
Dit komt overeen met 61 graden 30 minuten en 0 seconden.
```

Geeft men de hoek `25.75` in, dan verschijnt er:
```
Dit komt overeen met 25 graden 45 minuten en 0 seconden.
```

Geeft men de hoek `25.755` in, dan verschijnt er:
```
Dit komt overeen met 25 graden 45 minuten en 18 seconden.
```

{: .callout.callout-info}
>#### Tip
> Door de manier waarop Python kommagetallen opslaat kan `25.755` eigenlijk als `25.75499999999` bewaard worden. Dit kan kleine probleempjes opleveren bij het uitvoeren van het programma. Je kan dit probleem opvangen door op *de juiste plaatsen* in de code af te ronden op 3 cijfers.

