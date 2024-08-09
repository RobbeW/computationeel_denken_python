## Gegeven

Het <a href='https://nl.wikipedia.org/wiki/Brits-Amerikaans_maatsysteem' target='_blanc'>Imperial (Standard) System</a> is een **niet**-standaard systeem van maten en gewichten.

Het verband tussen de lengtematen *inch*, *foot* en *yard* is als volgt.

|-----------+-------------+---------------|
| Imperial  | Grootte     | in SI-eenheid |
| --------- |-------------|:-------------:|
| 1 inch    |             | 2.54 cm       |
| 1 foot    | 12 inch     |               |
| 1 yard    | 3 feet      |               |
|-----------+-------------+---------------|
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}

## Gevraagd

Schrijf een programma dat voor aan de gebruiker een aantal meter vraagt. 

Daarna wordt er uitgerekend met hoeveel *yard*, *feet* en *inch* dit overeenkomt.

Zorg ervoor dat het aantal *feet* en het aantal *yard* een geheel getal is. Terwijl de kleinste eenheid *inch* een kommagetal (afgerond op 2 cijfers) kan zijn.

#### Voorbeeld 1
Voor een lengte van 1,80 m geldt:
```
Dit stemt overeen met 1 yard 2 feet 10.87 inch
```
Want 1 yard + 2 feet + 10,87 inch komt overeen met 1,80 m.

#### Voorbeeld 2
Terwijl voor een lengte van 2,21 m geldt:
```
Dit stemt overeen met 2 yard 1 feet 3.01 inch
```
Want 2 yard + 1 feet + 3,01 inch komt overeen met 2,21 m.

{: .callout.callout-info}
>#### Tips
> 
> - Er zijn meerdere oplossingsmethodes mogelijk. Een gemakkelijke manier is om de ingevoerde meters eerst om te rekenen naar inch. Vervolgens met je dit enkel nog verdelen over de feet en de yards.
> - Een kommagetal geheel maken doe je via `int()`. Zo is `int( 7.0 )` gelijk aan `7`.
