import math

# Vraag een kommagetal
x = float( input( 'Voer een getal in: ') )

# Bepaal y en z
y = math.floor( x )
z = y + 1

# Weergeven op het scherm
print(y, "≤", x, "<", z)
