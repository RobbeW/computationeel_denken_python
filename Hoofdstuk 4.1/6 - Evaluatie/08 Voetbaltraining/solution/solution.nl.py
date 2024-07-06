# Invoer
N = int(input("Geef het aantal spelers in: "))
K = int(input("Geef het nummer van de startspeler in: "))
P = int(input("Geef het aantal passen in: "))

# Berekening van uiteindelijke nummer
R = (K + P) % N
if R == 0:
    R = N
    
# Weergave
print(f"De bal eindigt bij speler {R}")
