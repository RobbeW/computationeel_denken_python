t = int( input( "Enter T: " ) )
for i in range(t):
    b = int( input( "Enter number of animals" ) )
    ruimtes_str = input( "Enter animal spaces" )
    ruimtes = ruimtes_str.split()
    som = 0
    for ruimte in ruimtes:
        som += int( ruimte )
    print( i + 1, som )