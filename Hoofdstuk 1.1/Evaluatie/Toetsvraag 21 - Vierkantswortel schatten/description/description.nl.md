<div class="text-end">
    <a class="btn btn-filled with-icon" href="https://dodona.be/nl/courses/2419/" target="_blank"><i class="mdi mdi-backburger mdi-24" title="link"></i>Link naar de vorige oefeningen</a>
</div>

## Gegeven
Elke leerling kent wel de vierkantswortel van 25, maar hoe nauwkeurig kan iemand de vierkantswortel van 32 schatten? Het onderstaande is meteen duidelijk:

$$
\mathsf{ 5 = \sqrt{25} < \sqrt{32} < \sqrt{36} = 6}
$$

en dus kan je besluiten dat de vierkantswortel van 32 een kommagetal is dat begint met een 5, of $$\mathsf{\sqrt{32} \approx 5,\ldots}$$.

Er is echter een methode om ook een vrij goede schatting te maken van het eerste cijfer **na de komma**. Deze methode om een benadering te bepalen voor $$\mathsf{\sqrt{a}}$$ werkt als volgt:

- Zoek de grootste gehele $$\mathsf{b}$$, zodat $$\mathsf{b \leqslant \sqrt{a}}$$;
- Bereken nu $$\mathsf{c = a : b}$$;
- Bepaal tot slot het gemiddelde van $$\mathsf{b}$$ en $$\mathsf{c}$$ en rond af op één cijfer na de komma.


Voor het voorbeeld met $$\mathsf{a = 32}$$, bekomen we dus $$\mathsf{b = 5}$$ en $$\mathsf{c = 6,4}$$. Het gemiddelde van deze getallen is $$\mathsf{5,7}$$. De vierkantswortel van $$\mathsf{32}$$ met het rekentoestel uitrekenen levert ongeveer $$\mathsf{5,656\,854\ldots}$$ De schatting is dus zeer goed!

## Gevraagd
Schrijf een programma dat een natuurlijk getal aan de gebruiker vraagt en vervolgens via bovenstaande werkwijze een schatting bepaalt. Daarna wordt de schatting vergeleken met een nauwkeurige berekening (op 3 cijfers nauwkeurig).

#### Voorbeelden
Voor het getal `32` verschijnt er:
```
De vierkantswortel van 32 wordt geschat als 5.7 en is in werkelijkheid 3.657
```

Voor het getal `25` verschijnt er:
```
De vierkantswortel van 25 wordt geschat als 5.0 en is in werkelijkheid 5.0
```
