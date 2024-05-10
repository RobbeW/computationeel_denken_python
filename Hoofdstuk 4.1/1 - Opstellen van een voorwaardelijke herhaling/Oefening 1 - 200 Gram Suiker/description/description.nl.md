## Gegeven
Laura wil haar moeder helpen met het bakken van taarten. Ze gebruikt een eetlepel om 200 g suiker af te 'wegen'. Met elke eetlepel neemt Laura *ongeveer* 13 g.

![Suiker 'afwegen'.](media/sugar.gif "Suiker 'afwegen'."){:data-caption="Suiker 'afwegen'." width="250px"}

## Gevraagd

Na hoeveel lepels moet Laura stoppen om minimaal 200 g suiker af te wegen? *Simuleer* dit proces, maar hou rekening met onderstaande opmerking.

Omdat elke schep **niet exact even groot** is, gebruik je `random.randint(110, 150) / 10` om een willekeurige hoeveelheid suiker tussen 11 en 15 g af te 'wegen'.

Toon na elke schep hoeveel gram suiker Laura ongeveer heeft. **Rond** bij deze weergave **af** op één decimaal.

## Voorbeeld

De uitvoer van het programma *kan* het volgende zijn:

```
Na 1 lepels, heeft Laura 11.6 g suiker.
Na 2 lepels, heeft Laura 24.9 g suiker.
Na 3 lepels, heeft Laura 37.1 g suiker.
Na 4 lepels, heeft Laura 48.4 g suiker.
Na 5 lepels, heeft Laura 63.0 g suiker.
Na 6 lepels, heeft Laura 74.2 g suiker.
Na 7 lepels, heeft Laura 87.1 g suiker.
Na 8 lepels, heeft Laura 99.3 g suiker.
Na 9 lepels, heeft Laura 111.3 g suiker.
Na 10 lepels, heeft Laura 125.5 g suiker.
Na 11 lepels, heeft Laura 137.8 g suiker.
Na 12 lepels, heeft Laura 152.1 g suiker.
Na 13 lepels, heeft Laura 166.6 g suiker.
Na 14 lepels, heeft Laura 181.5 g suiker.
Na 15 lepels, heeft Laura 194.7 g suiker.
Na 16 lepels, heeft Laura 207.3 g suiker.
```

{: .callout.callout-info}
>#### Tip
>Vergeet de `random` module niet te importeren.
