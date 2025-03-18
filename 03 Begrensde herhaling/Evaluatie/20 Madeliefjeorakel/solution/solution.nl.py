aantal = int( input( "Geef het aantal bloemblaadjes in: " ) )

for i in range(aantal): 
    if i % 2 == 0:
        print("Hij houdt van me")
    else:
        print("Hij houdt niet van me")
