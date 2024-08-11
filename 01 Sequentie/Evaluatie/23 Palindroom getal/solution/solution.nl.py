# Invoer vragen aan de gebruiker
getal = int( input( 'Geef een getal van 3 cijfers in: ' ) )

# Eeuw bepalen
H = getal // 100
T = ( getal % 100 ) // 10 
E = getal % 10

palindroomgetal = getal * 10**3 + E * 10**2 + T * 10 + H

# Weergeven op het scherm
print( palindroomgetal, 'is een palindroomgetal.' )
