# Vraag een getal
getal = int( input( "Geef de getal in: " ) )

niet_priem = False # Ga ervan uit dat het getal priem is
for d in range(2, getal):
    niet_priem = niet_priem or getal % d == 0

if niet_priem:
    print(getal, "is niet priem.")
else:
    print(getal, "is priem.")
