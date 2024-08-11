# Invoer
aantal_per_dag= int( input( 'Hoeveel pilletjes moet u per dag nemen? ' ) )
aantal_doos= int( input( 'Hoeveel pilletjes zitten er in een doos? ' ) )

# Verwerking
aantal_dagen = aantal_doos // aantal_per_dag
overschot = aantal_doos % aantal_per_dag

# Weergave
print( 'U komt' , aantal_dagen, 'dag(en) toe.' )
print( 'U heeft' , overschot, 'pil(len) over.' )
