Na zoveel jaren geleden samen afgestudeerd te zijn, komen Jan en Piet mekaar tegen op een fuif voor gepensioneerden. Jan arriveerde in een
aftands 2pk-tje en Piet in het meest recente model van Maserati. Jan kon zijn ogen niet geloven en vraagt aan Piet: *gij waart vroeger net zo'n drinkebroer als ik en nu hebt ge het toch ver geschopt; hoe hebt ge dat klaargespeeld?* Daarop antwoordt Piet: *ik ben heel mijn leven blijven drinken, maar ik heb mijn leeggoed pas teruggebracht toen ik 65 was en toen was ik in één klap rijk!*

Leeggoed bijhouden lijkt dus wel te lonen. Je hebt diezelfde strategie gevolgd, en wil nu incasseren. Je bent echter alleen geïnteresseerd in... nog meer drank. Dus breng je een aantal bakken leeggoed van Spa terug naar de winkel en koopt daarmee een aantal volle bakken Spa, uiteraard minder dan je terugbracht. Na een tijdje levert dat genoeg nieuwe lege bakken op, en dan herhaal je die operatie. Hoe lang dat kan doorgaan hangt natuurlijk af van het aantal bakken leeggoed waarmee je begon, de prijs van een lege bak en de prijs van een volle bak. Op een bepaald moment is het gedaan, en dan heb je nog wat geld over. In deze opgave willen we weten hoeveel volle bakken je kan *kopen* met het aantal lege bakken waarmee je begon.

![Foto door Mathias Reding op Unsplash.](media/mathias-reding.jpg "Foto door Mathias Reding op Unsplash."){:data-caption="Foto door Mathias Reding op Unsplash." width="40%"}

## Opgave

Programmeer een functie `leeggoed(aantal, prijs_leeg, prijs_vol)` die gegeven een `aantal` stuks leeggoed, `prijs_leeg` de compensatie die je krijgt voor één stuk leeggoed en `prijs_vol` de prijs van een volle bak **het aantal volle bakken** dat je kan aankopen retourneert. (Er geldt altijd dat `prijs_vol` > `prijs_leeg`).

De vraag is dus, als je begint met `aantal` leeggoed en voortdurend het leeggoed inruilt voor *volgoed* (en wat geld eventueel), hoeveel eenheden kan je dan nog consumeren waarop je niet meer genoeg hebt om nog een volle bak aan te schaffen?

#### Voorbeelden

```python
>>> leeggoed(2, 2, 3)
2
```

Je hebt 2 stuks leeggoed; de prijs van 1 stuk leeggoed is € 2; de prijs vol is € 3. Je wisselt die 2 stuks leeggoed in (wat € 4 oplevert) tegen 1 vol en drinkt die bak Spa op; je hebt nu 1 stuk leeggoed en € 1. Daarmee kan je 1 volle bak kopen, die leegdrinken en wisselen voor cash en dan heb op op het einde 2 volle bakken gehad.


```python
>>> leeggoed(7, 1, 8)
0
```

Je hebt dan wel 7 stuks leeggoed, wat telkens € 1 oplevert. Helaas kost een volle bak meteen € 8. Je kan dus geen volle bakken aankopen.

{: .callout.callout-secondary}
>#### Bron
> Geïnspireerd op een oefening uit de Vlaamse programmeerwedstrijd 2021 - categorie 1.