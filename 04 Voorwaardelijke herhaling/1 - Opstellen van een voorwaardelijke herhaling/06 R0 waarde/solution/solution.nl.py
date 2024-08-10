import math

r_0 = float( input( "Geef de R0 waarde in: " ) )
n = int( input( "Geef het aantal besmette leerlingen in: " ) )

teller = 0
while n < 1200:
    teller += 1
    nieuwe_besmettingen = math.floor(n*r_0)
    n += nieuwe_besmettingen
    print("Na", teller, "cycli zijn er", n, "besmettingen.")
