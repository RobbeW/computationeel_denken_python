## Gegeven
De plaatselijke bibliotheek registreert alle nieuwe boeken in hun digitale systeem.

Voor elk boek moeten ze een **cataloguscode** samenmstellen met dit patroon:

**GENRE-KLEUR-NUMMERCONTROLE**

- GENRE = afkorting van het genre (bv. `FIC`, `SCI`, `BIO`)
- KLEUR = tweekleurige code (bv. `RD`, `BL`, `GR`)
- NUMMER = viercijferig volgnummer (bv. `4567`)
- CONTROLE = controlegetal (1 cijfer)

## Opgave
Schrijf een programma dat vraagt naar:

- de **titel** van het boek;
- de **genre-afkorting** (bv. `FIC`, `SCI`, `BIO`);
- de **kleurcode** (bv. `RD`, `BL`, `GR`);
- het **viercijferige nummer**;
- het **controlegetal** (1 cijfer).

Het programma moet vervolgens:

- de **volledige cataloguscode** samenstellen in de vorm `GENRE-KLEUR-NUMMERCONTROLE`;
- één zin afdrukken waarin de code gekoppeld wordt aan de titel van het boek.

Gebruik exact dezelfde tekststructuur als in het voorbeeld.

## Voorbeeld

Bij invoer:
```text
Harry Potter
FIC
BL
4567
9
```

Is de uitvoer: 
```
Het boek met cataloguscode FIC-BL-45679 heeft als titel: Harry Potter.
```