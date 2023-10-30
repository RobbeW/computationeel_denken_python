aantalStappen = int( input( 'Hoeveel stappen moet je nog zetten?' ) )

teDoen = 10000 - aantalStappen

if( aantalStappen < 9999 ):
    print('Je dient nog', teDoen, 'stappen te zetten.')
elif (aantalStappen == 9999):
    print('Je moet maar één stap meer zetten.')
else: 
    print('Je hebt je stappendoel van vandaag reeds bereikt.')