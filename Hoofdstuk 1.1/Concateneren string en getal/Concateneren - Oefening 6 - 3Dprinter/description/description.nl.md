## Gegeven

Bij een 3D-printer worden de motoren bestuurd door kleine electronica bordjes genaamd *drivers*. De A4988 is een van de meeste gebruikte drivers. Opdat de driver goed werkt moet de elektrische spanning V<span style="vertical-align: sub;">ref</span> correct worden ingesteld. Dit gebeurt met de volgende formule:

$$
V_{\text{ref}} = 8\cdot 0,05 \cdot I
$$

waarbij I de stroomsterkte voorstelt die de motor nodig heeft.

![Een 3D-printer.](media/3dprinter.jpg "Foto door Kadir Celep op Unsplash."){:data-caption="Een 3D-printer." width="30%"}

## Gevraagd

Schrijf een programma dat voor een ingelezen V<span style="vertical-align: sub;">ref</span> de stroomsterkte uitrekent.

#### Voorbeeld
Bij invoer `0.574` als V<span style="vertical-align: sub;">ref</span> verschijnt als uitvoer:
```
De stroomsterkte is 1.4349999999999998
```