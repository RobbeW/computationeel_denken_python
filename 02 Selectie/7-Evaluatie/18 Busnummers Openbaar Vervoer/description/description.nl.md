Bij **De Lijn** worden busritten aangeduid met een combinatie van een **lijnnummer** en een **ritnummer**.

* Het **lijnnummer** bestaat uit één tot drie cijfers en kan soms een letter bevatten (bijvoorbeeld `3`, `28`, `6A`, `88B`).
* Het **ritnummer** is een administratief nummer van **vier cijfers**, dat één specifieke rit binnen een lijn identificeert.

Wanneer deze twee elementen worden gecombineerd, ontstaat een **ticketcode** die uniek naar één bepaalde busrit verwijst.


## Opgave
Schrijf een programma dat:

* Aan de gebruiker vraagt wat de **bestemming** is van de busreis;
* Daarna het **lijnnummer** opvraagt;
* Vervolgens het **ritnummer** opvraagt (een reeks van **vier cijfers**);
* Op basis hiervan een **ticketcode** samenstelt;
* Tenslotte op een duidelijke manier het resultaat weergeeft op het scherm.


#### Voorbeeld

Bij volgende invoer:
```
Gent Zuid
3
0453
```

Verschijnt er:
```
De bus naar Gent Zuid heeft lijn 3.
De ticketcode is: 30453
```