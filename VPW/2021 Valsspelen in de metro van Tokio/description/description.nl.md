
Net zoals in vele steden met een metro moet je in Tokio je kaart scannen bij het binnenkomen en bij het buitengaan: het bedrag dat van je prepaid kaart afgaat hangt enkel af van je start- en eindstation, niet van welke stations je onderweg nog aandeed. Je mag inderdaad gelijk welke route volgen, bijvoorbeeld om je favoriete sushi-stand te bezoeken, zolang je het station maar niet verlaat. De prepaid kaarten in Tokio zijn naamloos, en, echt op zijn Belgisch, kwamen we direct op het idee voor een app die een groep mensen in staat stelt wat minder te betalen, namelijk door onderweg kaarten te wisselen.

Hier is een extreem geval: Kenji moet 's morgens van station Shibuya naar station Asakusa; dat kost 4 eenheden. Terzelfdertijd moet Ronin van
Asakusa naar Shibuya, ook 4 eenheden. Samen betalen ze 8 eenheden. Maar als ze mekaar onderweg ontmoeten, bijvoorbeeld in Shimbashi, en daar dan hun kaarten wisselen, dan komt elke kaart aan waar die vertrok, en is de totale kost 0, of de totale winst is 8. 's Avonds reizen ze omgekeerd, wisselen weer van kaart en iedereen is gelukkig, behalve de uitbaters van de metro.

## Opgave
De app die jullie gaan ontwikkelen heeft een inschrijfmodule voor een bepaald tijdsslot: daarin geven een aantal mensen hun begin- en eindstation op. De app berekent vervolgens hoe de kaarten moeten gewisseld worden en toont de totale winst. Uiteraard mag het niet zo zijn dat sommige individuen verlies lijden: zie daarvoor de invoer later.

Stations worden gegeven als een positief getal, van 1 tot N, het aantal stations. De prijs tussen twee stations komt in de vorm van een matrix, geïndexeerddoor de stations. Deze matrix krijg je helemaal: hij is telkens symmetrisch met nullen op de diagonaal en elders enkel strikt positieve gehele getallen.

Als uitvoer verwachten we de maximale totale winst die geboekt kan worden door kaarten te wisselen zonder dat er iemand verlies lijdt.

#### Voorbeelden
De eerste regel stelt het aantal testgevallen voor. Per testgeval volgt

- een regel met het aantal stations N; N > 1
- de kostenmatrix: N regels met telkens N positieve getallen gescheiden door een blanco; enkel op de diagonaal staan nullen
- een regel met het aantal personen P dat inschreef op de app: die personen zijn genummerd van 1 tot P; P > 0
- dan komt één regel met de P vertrekstations van de P personen, gescheiden door een blanco
- dan komt één regel met de P eindstations gescheiden door een blanco

```
2
5
0 1 2 3 4
1 0 2 3 4
2 2 0 4 1
3 3 4 0 1
4 4 1 1 0
3
1 2 5
5 3 1
3
0 4 6
4 0 4
6 4 0
2
1 2
2 3
```

Als uitvoer verwachten we per testgeval één regel met daarop het volgnummer van het testgeval, een blanco, en dan de maximale totale winst die kan gemaakt worden zonder dat iemand verlies lijdt.

```
1 8
2 0
```

In eerste testgeval kunnen persoon 1 en 3 hun kaart wisselen en elk 4 eenheden winst maken: persoon 2 wisselt niet, want daardoor wordt het niet globaal beter.
In het tweede testgeval is de totale kost zonder verwisselen van kaarten 8. Door de kaarten te wisselen wordt de totale kost 6 en dat is beter, maar de kaart van de eerste persoon wordt in dit scenario met 6 gedebiteerd i.p.v. 4 en dat wil die natuurlijk niet. Hier kan geen winst gemaakt worden.