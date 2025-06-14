def leeggoed(aantal, prijs_leeg, prijs_vol):
    totaal = aantal * prijs_leeg
    vol = 0 # bepaalt het totaal aantal volle bakken dat gekocht werd (volgoed)
    
    while totaal >= prijs_vol:
        vol += totaal // prijs_vol
        
        overschot = totaal % prijs_vol
        totaal = (totaal // prijs_vol) * prijs_leeg + overschot
    
    return vol
