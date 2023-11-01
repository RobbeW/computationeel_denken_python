t = int( input(  ) )
for i in range(t):
    max = int( input( ) )
    tekst = input( )
    woorden = tekst.split()

    str = woorden[0]
    som = 0
    for j in range(1,len(woorden)):
        woord = woorden[j]
        if len(str + " "+woord) <= max:
            str += " "+woord
        else:
            som += (max - len(str) )**2
            str = woord           
    som += (max - len(str) )**2
    
    print( i + 1, som )
