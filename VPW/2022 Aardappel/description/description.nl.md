Wanneer ik aardappelen kook wil ik graag dat de stukken aardappel ongeveer even snel gaar zijn: ik wil geen halfgare en overgare aardappelen op mijn bord. Daarom snijd ik die aardappelen in stukken tot de stukken hoogstens een vooraf bepaalde grootheid `G` verschillen. Ik heb namelijk een systeem uitgedokterd om aan aardappelen een grootte toe te kennen en dat is altijd een geheel getal. Dat maakt het vergelijken van die aardappelen gemakkelijk en ook de procedure om een aardappel (of een stuk aardappel) in twee stukken te snijden: als de grootte even is, dan snij ik in twee gelijke delen.

![De oneindige aardappelsnijder.](media/potato.gif "De oneindige aardappelsnijder."){:data-caption="De oneindige aardappelsnijder." width="400px"}

Als de grootte oneven is, dan snij ik in twee delen die juist één grootheid verschillen. Dus, een (stuk) aardappel van grootte 8 snij ik (als het nodig is) in twee stukken van 4. Een (stuk) aardappel van grootte 9 snij ik in een stuk van 4 en eentje van 5. 

Gegeven de grootte van de initiële aardappelen, en `G`, hoeveel keer moet ik een (stuk) aardappel doorsnijden?

## Opgave
Schrijf een functie `aardappel(groottes, G)` die voor een lijst met groottes van aardappelen en een voorop gegeven maximale grootteverschil `G` het aantal snijbeurten zoekt zodat de aardappelen hoogstens `G` van elkaar verschillen.

Bestudeer onderstaande voorbeelden grondig.

#### Voorbeelden

```python
>>> aardappel([2, 4, 7], 3)
3
```

```python
>>> aardappel([4, 8, 14], 2)
4
```

```python
>>> aardappel([5, 7, 11, 13], 1)
10
```

{: .callout.callout-secondary}
>#### Bron
> Geïnspireerd op een oefening uit de Vlaamse programmeerwedstrijd 2022 - categorie 1.