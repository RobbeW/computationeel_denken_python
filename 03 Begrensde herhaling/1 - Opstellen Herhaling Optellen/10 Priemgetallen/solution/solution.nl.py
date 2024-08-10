# Vraag een bovengrens
grenswaarde = int( input( "Geef de grenswaarde in: " ) )

# Inleidende weergave
print("De priemgetallen kleiner dan", grenswaarde, "zijn:")
teller = 0
# Ga door de getallen van 2 tot het getal
for i in range(2, grenswaarde):
    
    niet_priem = False # Ga ervan uit dat het getal priem is
    for d in range(2, i):
        niet_priem = niet_priem or i % d == 0
    
    if not niet_priem:
        teller += 1
        print(i)
    
print( "Er werden", teller, "priemgetallen gevonden." )
