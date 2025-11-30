## Gegeven
Deelbaarheid door **9** heeft een verrassende eigenschap.

Neem een natuurlijk getal kleiner dan 1000 (dus tussen **1 en 999**).  
Schrijf het als honderden, tientallen en eenheden:

* `H` = aantal **honderdtallen** (bijvoorbeeld 963 → H = 9)
* `T` = aantal **tientallen** (963 → T = 6)
* `E` = aantal **eenheden** (963 → E = 3)

Als je nu de **som** `H + T + E` aftrekt van het oorspronkelijke getal `n`, dan blijkt dat **verschil** altijd deelbaar te zijn door 9.

Voorbeeld voor `n = 963`:

* H = 9, T = 6, E = 3
* verschil = 963 − 9 − 6 − 3 = 945
* 945 is deelbaar door 9.

## Opgave
Schrijf een programma dat:

* Een **geheel getal** inleest dat **kleiner is dan 1000** en **groter dan of gelijk aan 1**;
* De waarden van **H**, **T** en **E** berekent;
* Het **verschil** berekent van het getal en `(H + T + E)`;
* **H, T, E, het verschil** en of het verschil **deelbaar is door 9** afdrukt.

Bij een ongeldige invoer (0 of kleiner, of 1000 of groter) moet een duidelijke foutmelding getoond worden.

#### Voorbeelden

Voor invoer:
```
754
```
Verschijnt er: 
```
Honderdtallen: 7, Tientallen: 5, Eenheden: 4
Verschil = 738
738 is deelbaar door 9.
```

Voor invoer:
```
0
```
Verschijnt er: 
```
Ongeldige invoer: het getal moet groter zijn dan 0.
```

Voor invoer:
```
1000
```
Verschijnt er: 
```
Ongeldige invoer: het getal moet kleiner zijn dan 1000.
```
