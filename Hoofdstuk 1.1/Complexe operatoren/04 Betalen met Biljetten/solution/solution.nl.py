# Vraag de gebruiker naar het te betalen bedrag
bedrag = int( input( "Voer het te betalen bedrag in euro's in: " ) )

# Bereken het aantal biljetten en munten
aantal_vijftig = bedrag // 50
restbedrag = bedrag % 50

aantal_twintig = restbedrag // 20
restbedrag %= 20

aantal_tien = restbedrag // 10
restbedrag %= 10

aantal_vijf = restbedrag // 5
restbedrag %= 5

aantal_twee = restbedrag // 2
aantal_een = restbedrag % 2

print()
# Print het aantal benodigde biljetten en munten
print( 'biljet 50:', aantal_vijftig )
print( 'biljet 20:', aantal_twintig )
print( 'biljet 10:', aantal_tien )
print( 'biljet 5:', aantal_vijf )
print( 'munt 2:', aantal_twee )
print( 'munt 1:', aantal_een )
