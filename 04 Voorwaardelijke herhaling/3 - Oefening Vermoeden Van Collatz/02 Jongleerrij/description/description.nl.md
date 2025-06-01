## Gegeven
Men definieert een rij getallen waarbij men start met een willekeurig natuurlijk getal $$\mathsf{a}$$ (> 0) als volgt:

- als het getal even is, bereken dan $$\mathsf{\sqrt{a}}$$ en rond af naar beneden;
- als het getal oneven is, bereken dan $$\mathsf{\sqrt{a^3}}$$ en rond af naar beneden.

Neem dit uitkomst van deze bewerking als nieuw getal en herhaal het proces. Men **vermoedt** dat dit proces uiteindelijk steeds eindig bij 1...

## Gevraagd

Schrijf een programma dat aan de gebruiker het startgetal vraagt en nadien telkens het volgende getal bepaalt. Elke waarde wordt op het scherm weergegeven en het programma stopt bij 1.

#### Voorbeelden

Bij invoer 3 verschijnt er:

``` 
3
5
11
36
6
2
1
``` 


{: .callout.callout-primary}
>#### Trivia
> Men noemt dit een jongleerrij, omdat de rij getallen opeenvolgend stijgt en daalt, net zoals de ballen in de hand van een jongleur.
>
> ![Een jongleur.](media/juggler.gif "Een jongleur."){:data-caption="Een jongleur." width="250px"}
