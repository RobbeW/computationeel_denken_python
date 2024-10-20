def klaverjassen(troef, kaarten):
    dict = {"B": (20,2),
            "9": (14,0),
            "A": (11,11),
            "T": (10,10),
            "H": (4,4),
            "D": (3,3),
            "8": (0,0),
            "7": (0,0)}
    waarde = 0
    for kaart in kaarten:
        soort = kaart[0]
        symb = kaart[1]
        if soort == troef:
            i = 0
        else:
            i = 1
        waarde += dict[symb][i]
    
    return waarde
