def punten( kaart, troef):
    dict = {"B": (20,2),
            "9": (14,0),
            "A": (11,11),
            "10": (10,10),
            "H": (4,4),
            "D": (3,3),
            "8": (0,0),
            "7": (0,0)}
    soort = kaart[0]
    kaart = kaart[1]
    index = 0 if soort == troef else 1
    return dict[kaart][index]  

t = int( input(  ) )
for i in range(t):
    troef = input( )
    kaarten_str = input( )
    kaarten = kaarten_str.split()
    som = 0
    for kaart in kaarten:
        som += punten(kaart, troef)
    print( i + 1, som )
