## Gegeven
Indien men een bal vanop een bepaalde hoogte laat vallen dan stuitert die totdat deze uiteindelijk stil komt te liggen.

<div class="hidden-print">
    <div class="dodona-centered-group">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/6-Zpa7CJe5Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
</div>

Voor verschillende soorten ballen geldt een restitutiecoëfficiënt $$\mathsf{c}$$. Dit is een kommagetal tussen 0 en 1 dat aangeeft hoe ver de bal terugbotst. Een waarde van 1 betekent dat de bal perfect terugbotst terwijl 0 betekent dat de bal meteen tot rust komt.

Het volgende verband bestaat tussen $$\mathsf{c}$$, de hoogte $$\mathsf{h_i}$$ en de hoogte $$\mathsf{h_{i+1}}$$ na 1 keer botsen.

$$
\mathsf{c = \sqrt{\dfrac{h_{i+1}}{h_i}}}
$$

## Gevraagd

Schrijf een programma dat in **volgorde** de beginhoogte (in cm) van de bal en de restitutiecoëfficiënt vraagt. Vervolgens wordt afgedrukt na hoeveel botsingen de bal **minder dan 1 cm** boven de grond komt. 

Na elke botsing geef je de hoogte van de bal weer, deze hoogte rond je af op 1 decimaal.

#### Voorbeeld

Bij een starthoogte van `100.0` cm en een restitutiecoëfficient van `0.7` verschijnt er:

```
Na 1 botsing is de hoogte nog 49.0 cm.
Na 2 botsingen is de hoogte nog 24.0 cm.
Na 3 botsingen is de hoogte nog 11.8 cm.
Na 4 botsingen is de hoogte nog 5.8 cm.
Na 5 botsingen is de hoogte nog 2.8 cm.
Na 6 botsingen is de hoogte nog 1.4 cm.
Na 7 botsingen is de hoogte nog 0.7 cm.
```

{: .callout.callout-info}
>#### Tips
> - Hou in een aparte variabele het aantal botsingen bij.
> - Rond enkel af bij het afdrukken.
> - Je zal de formule moeten omvormen. Beide leden kwadrateren leidt tot:
>
>$$\mathsf{c^2 = \dfrac{h_{i+1}}{h_i}}$$
