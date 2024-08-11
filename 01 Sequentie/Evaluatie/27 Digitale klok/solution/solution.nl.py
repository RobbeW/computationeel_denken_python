# Invoer van een aantal seconden
sec = int( input( 'Geef het aantal seconden in: ' ) )

# Berekeningen
uren = sec // ( 60 * 60 )
minuten = (sec - uren * 60 * 60) // 60
seconden = sec % 60

# Uitvoer
print(uren, ":", minuten, ":", seconden)
