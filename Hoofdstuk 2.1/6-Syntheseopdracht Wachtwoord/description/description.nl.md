## Gegeven: 
Er is een correcte gebruikersnaam en wachtwoord om toegang te krijgen tot het systeem van het bedrijf.

## Gevraagd: 
Schrijf een programma dat vraagt naar de gebruikersnaam en het wachtwoord `(== input-functie)`;
Controleer of de ingevoerde `gebruikersnaam` en `wachtwoord` juist zijn;
Print een van de volgende berichten af:
* 'Toegang verleend' als de `gebruikersnaam` **en** het `wachtwoord` correct zijn;
* 'Incorrect wachtwoord' als alleen het `wachtwoord` foutief is;
* 'Incorrecte gebruikersnaam' als alleen de `gebruikersnaam` foutief is;
* 'Incorrecte gebruikersnaam en wachtwoord' als zowel de `gebruikersnaam` als het `wachtwoord` foutief zijn.


## Invoer: 
```
Voer uw gebruikersnaam in: janedoe
Voer uw wachtwoord in: wachtwoord123


```
## Uitvoer: 
```
Toegang verleend
```

{: .callout.callout-success}
>## Tips: 
>* Gebruik de `input()-functie` om de gebruiker naar de `gebruikersnaam` en het `wachtwoord` te vragen.
>* Gebruik voorwaardelijke uitspraken (`if`, `elif`, `else`) met de operatoren `and` en `or` om te bepalen welke beoordeling hoort bij de ingevoerde `gebruikersnaam` en het `wachtwoord`.
>* Print de beoordeling naar het scherm met behulp van de print()-functie.
