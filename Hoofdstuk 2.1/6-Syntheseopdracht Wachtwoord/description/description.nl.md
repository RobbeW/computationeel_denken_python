In <a href="https://www.theguardian.com/technology/2013/nov/07/adobe-password-leak-can-check" target="_blank">2013</a> werd de databank met gebruikersgevens van Adobe gehacked. Van maar liefst 150 miljoen accounts werden de emailadressen en bijbehorende wachtwoorden (met hints) buit gemaakt. In de databank werden de wachtwoorden versleuteld, maar doordat het versleutelingsalgoritme eenvoudig was, werden de wachtwoorden al snel gekraakt.

Hier vind je een (gecensureerd) voorbeeld van vijf buitgemaakte accounts uit deze beroemde hack:

```
aut?????mer@yahoo.com           BB4e6X+b2xLioxG6CatHBw
fer?????graciliano@hotmail.com  Cm8mAzxAiwzioxG6CatHBw
wit?????adowski@gmail.com       n+TZlu41zyHioxG6CatHBw
iso?????@gmail.com              FAniAwP+U13ioxG6CatHBw
oja?????rga2@yahoo.com          kxiV+a47bSlf+E5Ulu/AzA
```

![De hoofdkantoren van Adobe in San Jose (Californië).](media/adobe_hq.jpg "De hoofdkantoren van Adobe in San Jose (Californië)."){:data-caption="De hoofdkantoren van Adobe in San Jose (Californië)." width="40%"}

Indien het versleutelingsmechanisme wel goed is, dan werkt een loginprocedure *(ongeveer)* als volgt:

- Vraag naar de gebruikersnaam en het wachtwoord.
- Controleer of deze gebruikersnaam bestaat en indien ja, haal het **versleutelde wachtwoord** op.
- Gebruik hetzelfde versleutelingsmechanisme om het ingetikte wachtwoord van de gebruiker om te zetten naar een versleutelde versie.
- Vergelijk daarna beide versleutelde wachtwoorden.

## Gevraagd
Schrijf een programma dat vraagt naar de gebruikersnaam en het wachtwoord en controleer vervolgens of dit overeenkomt met de gegevens van gebruiker `janedoe`. Er werd onderaan een eenvoudig versleutelingalgoritme gegeven, je kan dit gebruiken via `versleutel( wachtwoord )`. Het resultaat van deze (eigen functie) is een **versleutelde** versie van de variabele `wachtwoord`.

Print een van de volgende berichten af:
- 'Incorrecte gebruikersnaam' als de `gebruikersnaam` foutief is;
- 'Toegang verleend' als de `gebruikersnaam` **en** het `wachtwoord` correct zijn;
- 'Incorrect wachtwoord' als alleen het `wachtwoord` foutief is;

#### Voorbeeld
```
Voer uw gebruikersnaam in: janedoe
Voer uw wachtwoord in: probeersel
```
leidt tot de uitvoer:
```
Incorrect wachtwoord
```
