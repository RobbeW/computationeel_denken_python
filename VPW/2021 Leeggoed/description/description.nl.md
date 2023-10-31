Na zoveel jaren geleden samen afgestudeerd te zijn, komen Jan en Piet mekaar tegen op een fuif voor gepensioneerden. Jan arriveerde in een
aftands 2pk-tje en Piet in het meest recente model van Maserati. Jan kon zijn ogen niet geloven en vraagt aan Piet: *gij waart vroeger net zo'n drinkebroer als ik en nu hebt ge het toch ver geschopt; hoe hebt ge dat klaargespeeld?* Daarop antwoordt Piet: *ik ben heel mijn leven blijven drinken, maar ik heb mijn leeggoed pas teruggebracht toen ik 65 was, en toen was ik in één klap rijk!*

Leeggoed bijhouden lijkt dus wel te lonen. Je hebt diezelfde strategie gevolgd, en wil nu incasseren. Je bent echter alleen geïnteresseerd in ... nog meer drank. Dus breng je een aantal bakken leeggoed van Spa terug naar de winkel en koopt daarmee een aantal volle bakken Spa, uiteraard minder dan je terugbracht. Na een tijdje levert dat genoeg nieuwe lege bakken op, en dan herhaal je die operatie. Hoe lang dat kan doorgaan hangt natuurlijk af van het aantal bakken leeggoed waarmee je begon, de prijs van een lege bak en de prijs van een volle bak. Op een bepaald moment is het gedaan, en dan heb je nog wat geld over. In deze opgave willen we weten hoeveel volle bakken je kan *kopen* met het aantal lege bakken waarmee je begon, en hoeveel geld je op het einde nog overhebt.


## Opgave

Meer precies: je begint met `B` stuks leeggoed. De prijs van één stuk leeggoed is `PrijsL`. De prijs van een stuk dat vol is (inbegrepen het leeggoed) is `PrijsV` (er geldt altijd dat `PrijsV` > `PrijsL`). Als je voortdurend leeggoed (en wat geld eventueel) inruilt voor volgoed (en wat geld eventueel), hoeveel eenheden volgoed kan je dan nog consumeren tot het ogenblik waarop je niet meer genoeg hebt om nog een eenheid volgoed aan te schaffen, en hoeveel geld heb je op dat ogenblik?

Als voorbeeld: je hebt 2 stuks leeggoed; de prijs van 1 stuk leeggoed is 2 euro; de prijs vol is 3 euro. Je wisselt die 2 stuks leeggoed in tegen 1 vol en drinkt die bak Spa op; je hebt nu 1 stuk leeggoed en 1 euro. Daarmee kan je 1 volle bak kopen, die leegdrinken en wisselen voor cash en dan heb op op het einde 2 volle bakken gehad, en heb je 2 euro over.

#### Voorbeelden
De eerste regel stelt het **aantal testgevallen** voor. Per testgeval volgt één lijn met daarop drie getallen gescheiden door een blanco; die getallen zijn

- `B`: het aantal stuks leeggoed (bakken bijvoorbeeld) waarmee je begint
- `PrijsL`: de prijs van één stuk leeggoed
- `PrijsV`: de prijs van één stuk volgoed

```
2
2 2 3
7 1 8
```

Per testgeval moet je één regel afdrukken: die begint met het volgnummer van het testgeval. Dan komt het aantal nieuwe stuks volgoed dat je je hebt kunnen aanschaffen volgens dat testgeval en daarna hoeveel euro je nog overhebt. De getallen worden gescheiden door één blanco.

```
1 2 2
2 0 7
```