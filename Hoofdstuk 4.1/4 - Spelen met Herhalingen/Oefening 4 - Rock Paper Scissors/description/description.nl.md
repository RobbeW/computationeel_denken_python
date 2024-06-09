Kan je winnen van de computer bij blad-steen-schaar?

## Opgave

Schrijf een programma waarbij je tegen de computer blad-steen-schaar speelt, totdat je als gebruiker `"stop"` intikt. Laat de gebruiker telkens ofwel `"blad"`, `"steen"` ofwel `"schaar"` intikken. Hou de score bij en geef die uiteindelijk weer op het scherm.

Geef de gebruiker 2 punten indien deze wint, 1 punt bij gelijkspel en 0 punten bij verlies.

![Blad steen schaar...](media/rock-paper-scissors.gif "Blad steen schaar..."){:data-caption="Blad steen schaar..." width="400px"}

#### Voorbeeld

Stel dat je als gebruiker de eerste keer `"blad"` intikte. De computer koos willekeurig voor `"schaar"`, dan verschijnt er:

```
De computer koos: schaar
Je verliest!
```

De gebruiker tikt nogmaals `"blad"` in, er verschijnt vervolgens bijvoorbeeld:

```
De computer koos: blad
Gelijkspel!
```

De gebruiker tikt nogmaals `"blad"` in, er verschijnt vervolgens bijvoorbeeld:

```
De computer koos: steen
Je wint!
```

Indien de gebruiker nadien `"stop"` intikt verschijnt er:

```
Je score was 3 op 6
```