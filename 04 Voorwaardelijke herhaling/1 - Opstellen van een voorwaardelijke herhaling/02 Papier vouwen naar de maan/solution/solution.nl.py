d = float( input( "Geef de dikte van het blad papier in (in cm): " ) )
afstand = int( input( "Geef de afstand in (in km): " ) )

i = 0
while d / 100000 < afstand:
    i = i + 1
    d = d * 2
    if i == 1:
        print("Na", i, "vouw bedraagt de dikte", round(d, 3), "cm.")
    else:
        print("Na", i, "vouwen bedraagt de dikte", round(d, 3), "cm.")
    
print("Het blad moest", i, "keer gevouwen worden.")
