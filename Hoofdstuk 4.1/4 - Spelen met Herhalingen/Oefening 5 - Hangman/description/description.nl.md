<a href="https://nl.wikipedia.org/wiki/Galgje" target="_blank">Galgje</a> is een spelletje waarbij een woord geraden moet worden, door individuele letters te raden. De spelers mogen maar een beperkt aantal fouten maken, de fouten worden vaak weergeven door een hangend mannetje aan een galg te tekenen.

![Galgje](media/hangman.png "Galgje"){:data-caption="Galgje" .light-only width="45%"}

![Galgje](media/hangman_dark.png "Galgje"){:data-caption="Galgje" .dark-only width="45%"}

## Opgave

Programmeer dit spelletje. Bestudeer grondig onderstaande voorbeeld om de verschillende stappen te implementeren. Je mag ervan uitgaan dat de woorden die genomen worden telkens uit **acht tekens** bestaan. Het programma stopt automatisch indien er 10 fouten gemaakt werden.

Enkele **tips**:

- Het stukje code dat klaar staat haalt uit een lijst van quasi 200 woorden een willekeurig woord op.
- Je kan gemakkelijk itereren over een stukje tekst via:

  ```python
for i in range(8):
    letter = woord[i]
  ```

- Gebruik de vorige `for` loop om te controleren of de gok gelijk is aan een letter.

- Om de vraagtekens te vervangen door het gokje `gok` (indien dit correct is) kan je de volgende code gebruiken:

  ```python
tijdelijk = list(tekens)
tijdelijk[i] = gok           # vervangt het ? op plaats i door de gok
tekens = "".join(tijdelijk)  # slaat dit opnieuw op in de variabele tekens
  ```

- In de sandbox kan je niet gebruik maken van de grote lijst met 200 woorden. Gebruik daar een vast woord om het programma te testen.

#### Voorbeeld

![Een implementatie van galgje.](media/hangman.gif "Een implementatie van galgje."){:data-caption="Een implementatie van galgje." .dark-only width="500px"}

![Een implementatie van galgje.](media/hangman_inverted.gif "Een implementatie van galgje."){:data-caption="Een implementatie van galgje." .light-only width="500px"}