import random

# stel de parameters in
bedrag = random.randint(500, 1001)
aantal_jaren = int(input("Hoeveel jaar wilt u sparen? "))
interest_per_jaar = 2.0

for i in range (aantal_jaren): 
    print('Na', i, 'jaar staat er', round(bedrag, 2), 'euro op de rekening.')
    bedrag *= ( 1 + interest_per_jaar/100 )

# druk het resultaat af op het scherm
print("Na", aantal_jaren, "jaar sparen aan een interest van", interest_per_jaar, "% staat er", round(bedrag, 2), "euro op de spaarrekening.")
