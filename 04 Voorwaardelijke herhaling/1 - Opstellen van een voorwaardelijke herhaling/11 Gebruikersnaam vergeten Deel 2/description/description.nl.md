## Gegeven
In een voorgaande oefening ging het erover dat één emailadres gemiddeld gesproken met wel 130 verschillende accounts gekoppeld is. Een gebruikersnaam vergeten is dus niet abnormaal. Veel websites beschikken over de mogelijkheid om je gebruikersnaam naar je emailadres te laten verzenden.

## Gevraagd
Schrijf een programma dat vraagt naar het emailadres **en** de gebruikersnaam en vervolgens controleert of dit overeenkomt met de gegevens van gebruiker `janedoe`.

Print een van de volgende berichten af:
- 'Emailadres niet gekend.' als het `emailadres` foutief is;
- 'Gebruiker en email komen niet overeen.' als het `emailadres` niet correspondeert met de `gebruikersnaam`;
- 'Resetlink verstuurd.' als het `emailadres` **en** de `gebruikersnaam` overeenkomen.

Indien het emailadres foutief is, of niet correspondeert met de gebruikersnaam dan mag je opnieuw proberen. Er worden **maximaal drie pogingen** toegestaan.

#### Voorbeeld
Stel dat de gebruiker intikt:
```
Voer uw emailadres in: janedoe@sintlievenscolege.be
Voer uw gebruikersnaam in: janedoe
```

dan verschijnt er
```
Gebruiker en email komen niet overeen.
Probeer opnieuw.
```

De tweede keer tikt de gebruiker in:
```
Voer uw emailadres in: janedoe@sintlievenscollege.be
Voer uw gebruikersnaam in: janedoe
```

er verschijnt vervolgens:
```
Resetlink verstuurd.
```