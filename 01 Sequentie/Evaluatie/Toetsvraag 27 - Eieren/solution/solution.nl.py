# Invoer vragen aan de gebruiker
gros = int( input( 'Geef het aantal gross in: ' ) )
dozijn = int( input( 'Geef een aantal dozijn in: ' ) )
apart = int( input( 'Geef het aantal aparte eieren in: ' ) )

toevoeg = int( input( 'Geef het aantal toe te voegen eieren in: ' ) )

# aantallen berekenen
totaal = gros * 144 + dozijn * 12 + apart + toevoeg

gros = totaal // 144
rest = totaal % 144

dozijn = rest // 12
rest = rest % 12

# Weergeven op het scherm
print( 'Totale aantal eieren:', gros, 'gros,', dozijn, 'dozijn en', rest, 'eieren.' )
