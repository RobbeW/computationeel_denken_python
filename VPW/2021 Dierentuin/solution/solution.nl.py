t = int( input(  ) )
for i in range(t):
    b = int( input(  ) )
    ruimtes_str = input( )
    ruimtes = ruimtes_str.split()
    som = 0
    for ruimte in ruimtes:
        som += int( ruimte )
    print( i + 1, som )