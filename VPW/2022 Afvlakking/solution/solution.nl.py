t = int( input(  ) )
for i in range(t):
    str = input( )
    aantal = [int(n) for n in str.split()]
    som = 0
    for j in range(2, aantal[0]+1):
        if aantal[j] < aantal[j-1]:
            som += aantal[j-1] - aantal[j]
            aantal[j] = aantal[j-1]
    
    print( i + 1, som )
