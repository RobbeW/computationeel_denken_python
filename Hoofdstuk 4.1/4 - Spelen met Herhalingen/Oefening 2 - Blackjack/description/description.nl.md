## Gegeven
* We schrijven het algoritme om het kaartspel '21' te spelen. 
* Het programma geeft een gebruiker twee willekeurige getallen tussen 1 en 10 (1 en 10 inbegrepen).
* De som van die twee getallen wordt afgedrukt.

## Gevraagd

* Het programma vraagt nu telkens of de gebruiker nog kaarten wil; 
* Dit doet het programma totdat de gebruiker geen kaarten meer wil **of** totdat de som groter wordt dan 21;

Als de som:
* Gelijk is aan 19, ontvangt de gebruiker 2 euro;
* Gelijk is aan 20, ontvangt de gebruiker 5 euro;
* Gelijk is aan 21, ontvangt de gebruiker 10 euro;
* Groter is dan 21, verliest de gebruiker!

## Invoer
De gebruiker geeft steeds aan of hij/zij/hun nog een kaart wilt. 
Dit door middel van een van de volgende strings: 'ja', 'nee'.
Bijvoorbeeld: 

 ```
 De som bedraagt: ...
 Wil jij nog een kaart? 
 
 ```
 
 ## Uitvoer 
 Het programma drukt na elke beurt de nieuwe kaart en de huidige som af. Wanneer het spel eindigt wordt de winst of verlies afgedrukt. Bijvoorbeeld:
 ```
 De som bedraagt: ... 
```

{: .callout.callout-success}
>## Tips
>* Gebruik de `input()-functie` om de gebruiker om een actie te vragen.
>* Gebruik een `while-lus` om het spel te blijven spelen `zolang` de gebruiker kaarten wil en de som niet groter is dan 21.
>* Gebruik de `random.randint()-functie` om een willekeurige kaart te genereren tussen 1 en 10.
>* Houd de `som` bij in een variabele die je elke keer verhoogt met de waarde van de nieuwe kaart.
>* Print de som en de winst of verlies met behulp van de `print()-functie`; 
>* Gebruik `if`, `elif`en `else-statements` om te beslissen hoeveel de gebruiker wint. 
