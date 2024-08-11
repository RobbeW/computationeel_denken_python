aantal = int( input( "Geef het aantal schapen in: " ) )

for i in range(aantal): 
    if i == 0:
        print("1 schaap")
    else:
        print(f"{i+1} schapen")
