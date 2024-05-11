h_i = float( input( "Geef de beginhoogte (in cm) op: " ) )
c = float( input( "Geef de restitutiecoëfficiënt: " ) )

teller = 0
while h_i >= 1:
    teller += 1
    h_i = c**2 * h_i
    if teller == 1:
        print(f"Na {teller} botsing is de hoogte nog {round(h_i, 1)} cm.")
    else:
        print(f"Na {teller} botsingen is de hoogte nog {round(h_i, 1)} cm.")
