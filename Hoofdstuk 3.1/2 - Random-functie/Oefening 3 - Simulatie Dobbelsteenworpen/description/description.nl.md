## Gevraagd
* Schrijf een programma dat naar een **aantal worpen** vraagt;
* Vervolgens simuleert het programma evenveel worpen met **twee dobbelstenen**;
* Je berekent telkens de som van het aantal *ogen*;
* Op het einde wordt het gemiddelde van deze som berekend en op het scherm weergegeven. Je rondt hierbij af op 2 decimalen.

![Een worp van twee dobbelstenen.](media/dice.gif "Een worp van twee dobbelstenen."){:data-caption="Een worp van twee dobbelstenen." width="500px"}

#### Voorbeelden
Stel dat je `10` worpen simuleert. Aangezien het aantal ogen telkens tussen 2 en 12 ligt, zal het totale aantal ogen tussen 20 en 120 liggen. Het zou kunnen dat het totale aantal ogen tijdens die 10 worpen bijvoorbeeld 64 is. In dat geval verschijnt er:
```
Het gemiddelde bij 10 worpen is 6.4
```

Bij `10000` worpen is de uitvoer bijvoorbeeld:
```
Het gemiddelde bij 10000 worpen is 7.01
```

{: .callout.callout-info}
>#### Tips
>* Gebruik de `random.randint(a, b)` om een worp met één dobbelsteen te *simuleren*;
>* Houd de `som` van de worpen bij en bereken nadien het gemiddelde;
>* Vergeet niet om de `random` module eerst te importeren.
