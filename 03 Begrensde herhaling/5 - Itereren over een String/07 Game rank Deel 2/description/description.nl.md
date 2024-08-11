## Gegeven

Het vorige systeem is niet altijd even logisch. Zo zorgt de spelgeschiedenis `"WWLW"` voor een stijging van een rank. Je kan echter ook redeneren met een systeem van **wedstrijdpunten**:

De speler wint twee wedstrijdpunten, maar verliest nadien een wedstrijdpunt en komt zo op één wedstrijdpunt terecht. De vierde wedstrijd werd hier opnieuw een wedstrijdpunt aan toegevoegd. De speler eindigt dus met twee wedstrijdpunten wat niet genoeg is om een rank te stijgen.

## Gevraagd

Wijzig je algoritme naar dit systeem met wedstrijdpunten. Telkens een speler 3 wedstrijdpunten verdient heeft stijgt deze één rank. Indien de speler nul wedstrijdpunten heeft en daarna een wedstrijd verliest, dan zakt deze een rank. De wedstrijdpunten kunnen niet negatief zijn en de rank is steeds 0 of meer.

##### Voorbeelden

Indien de speler intikt: `"WWLW"` verschijnt er:

```
rank: 0
```

Indien de speler intikt: `"WWWWWLWW"` verschijnt er:

```
rank: 2
```

Tikt de speler in: `"LLLLLLWWLWW"` verschijnt er:

```
rank: 1
```

Tikt de speler in: `"WWLWLLWLLL"` verschijnt er:

```
rank: 0
```