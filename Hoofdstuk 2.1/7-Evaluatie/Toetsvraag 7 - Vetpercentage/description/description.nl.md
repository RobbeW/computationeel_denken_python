Het vetpercentage geeft de hoeveelheid vet die opgeslagen ligt in je lichaam. Een te hoog of te laag vetpercentage is ongezond. Een te hoog vetpercentage leidt tot verhoogde kans op hart- en vaatziekten en diabetes, maar ook een te laag vetpercentage is ongezond.

![Lichaamsvet.](media/towfiqu-barbhuiya.jpg "Afbeelding door Towfiqu barbhuiya op Unsplash."){:data-caption="Lichaamsvet." width="450px"}

Er zijn heel wat verschillende manieren om het vetpercentage te schatten. Onderstaande methode werd in 1969 bepaald door Jack H. Wilmore en Albert R. Behnke, deze methode geeft een vrij betrouwbare schatting van het vetpercentage. Men meet hierbij de buikhuidplooi $$\mathsf{Ab}$$ en de huidplooi van een bovenbeen $$\mathsf{Th}$$. Deze metingen (in mm) vult men in in onderstaande formule:

$$
\mathsf{ BD = 1,08543 - (0,000886 \cdot Ab) - (0,0004 \cdot Th) }
$$

Hierbij stelt $$\mathsf{BD}$$ de lichaamsdichtheid uit. Vervolgens kan men het **vetpercentage** uitrekenen met de formule van Siri (onderzocht door William E. Siri):

$$
\mathsf{ \dfrac{4,95}{BD} - 4,50 }
$$

Het hangt van de leeftijd af om te besluiten of dit te hoog of te laag is. Onderstaande tabel wordt gebruikt bij mannen. Bij mannen jonger dan 20 en 80 of ouder moet het vetpercentage op een andere manier berekend worden.

| Leeftijd | Gezonde percentages |
|:--------:|---------------------|
| 20 - 39  | 8% - 19%            |
| 40 - 59  | 11% - 21%           |
| 60 - 79  | 13% - 24%           |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

## Opgave
Schrijf een programma dat de twee metingen van de **huidplooien** aan vraagt, eerst de buikhuidplooi en vervolgens de huidplooi van een bovenbeen. **Daarna** wordt de **leeftijd** van de persoon gevraagd.
Het programma berekent vervolgens of de persoon een te hoog of te laag vetpercentage heeft. Je mag ervan uitgaan dat de gegevens van mannen afkomstig zijn.

#### Voorbeelden
Voor een man van 21 jaar met buikhuidplooi 15,8 mm en huidplooi van een bovenbeen 8,7 mm verschijnt er:
```
Het vetpercentage bedraagt 13.5 %.
Dit is een gezond vetpercentage.
```

Voor een man van 21 jaar met buikhuidplooi 27,8 mm en huidplooi van een bovenbeen 14,2 mm,verschijnt er:
```
Het vetpercentage bedraagt 19.14 %.
Dit vetpercentage is te hoog.
```

Voor een man van 18 jaar verschijnt er:
```
Er zijn betere methodes om het vetpercentage van deze persoon te berekenen.
```