## Gegeven
Op een grote promo-affiche van Albert Heijn staat:

"XXXXXL BONUS. 2+5 gratis. Da’s 7 halen, 2 betalen."

In de actie zitten dozen **vaatwastabletten** van **€5,99 per verpakking**.  
Tijdens de XXL BONUS-actie geldt:

* voor **elke 7 verpakkingen** in je winkelkar betaal je er **maar 2**;
* de andere **5 verpakkingen zijn dus gratis**;
* verpakkingen die **niet** in een volledige groep van 7 passen, betaal je aan **volle prijs**.

Daarnaast zijn er **twee extra kortingscodes**:

* Code `hamster20` geeft **20% extra korting** als je **minstens 2 verpakkingen** koopt.
* Code `hamster30` geeft **30% extra korting** als je **minstens 7 verpakkingen** koopt.
* In alle andere gevallen is er **0% extra korting**.

De extra korting wordt berekend op het **bedrag na de XXL BONUS-actie**.  
De eindprijs wordt afgerond op **2 cijfers na de komma**.

## Opgave
Schrijf een programma dat:

* Het **aantal verpakkingen** vaatwastabletten **vraagt**;
* Daarna een **kortingscode** inleest (bijvoorbeeld `hamster20`, `hamster30`);
* Eerst het **aantal te betalen verpakkingen na de XXL BONUS-actie** berekent;
* De **extra korting in procent** bepaalt op basis van het aantal verpakkingen en de kortingscode;
* De **eindprijs met korting** berekent, afgerond op 2 cijfers na de komma;
* Het resultaat exact in deze vorm afdrukt:

* `Aantal verpakkingen: ...`
* `Te betalen verpakkingen na XXL BONUS-actie: ...`
* `De extra korting bedraagt ... % .`
* `De eindprijs is ... euro.`

## Voorbeelden

Voor invoer:
```
1
Geen kortingscode
```

Verschijnt er: 
```
Aantal verpakkingen: 1
Te betalen verpakkingen na XXL BONUS-actie: 1
De extra korting bedraagt 0 %.
De eindprijs is 5.99 euro.
```

Voor invoer:
```
7
HAMSTER30
```

Verschijnt er: 
```
Aantal verpakkingen: 7
Te betalen verpakkingen na XXL BONUS-actie: 2
De extra korting bedraagt 30.0 %.
De eindprijs is 8.39 euro.
```
