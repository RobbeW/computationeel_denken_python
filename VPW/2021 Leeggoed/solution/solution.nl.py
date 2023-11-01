t = int( input(  ) )
for i in range(t):
    leeggoed_str = input( )
    lg = [int(n) for n in leeggoed_str.split()]
    totaal = lg[0] * lg[1]
    vol = 0 # bepaalt het totaal aantal volle bakken dat gekocht werd (volgoed)
    while totaal >= lg[2]:
        vol += totaal // lg[2]
        totaal = totaal % lg[2] + (totaal //lg[2])*lg[1]
    
    print( i + 1, vol, totaal )
