# Vraag de gebruiker om een decimaal getal
a = int( input( "Voer een ondergrens in: " ) )
b = int( input( "Voer een bovengrens in: " ) )
getal = float( input( "Voer een decimaal getal in: " ) )

# Controleer of het getal tussen a (inbegrepen) en b (niet inbegrepen) ligt
if a <= getal < b:
    print("Het getal", getal, "behoort tot [" + str(a) +", " + str(b)+"[.")
else:
    print("Het getal", getal, "behoort niet tot [" + str(a) +", " + str(b)+"[.")
