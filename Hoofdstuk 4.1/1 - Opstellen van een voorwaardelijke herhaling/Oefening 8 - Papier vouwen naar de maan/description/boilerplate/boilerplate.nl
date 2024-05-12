# Vraag de dikte van een blad papier
d = float( input( "Geef de dikte van het blad papier in (in cm): " ) )

# Herhaal het verdubbelen 42 keer
for i in range(42):
    d = d * 2
    if i == 0:
        print("Na", i+1, "vouw bedraagt de dikte", round(d, 3), "cm.")
    else:
        print("Na", i+1, "vouwen bedraagt de dikte", round(d, 3), "cm.")

# Toon de dikte in km
print("Uiteindelijk werd een dikte van", round(d / 100000, 3), "km bereikt.")