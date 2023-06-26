import random

# stel de parameters in
startbedrag = random.randint(500, 1001)
aantal_jaren = int(input("Hoeveel jaar wilt u sparen? "))
interest_per_jaar = 2.0

for i in range (0, aantal_jaren): 
    startbedrag *= 1.02
    print('Na', i, 'jaar staat er', startbedrag, 'euro op de rekening.')


# druk het resultaat af op het scherm
print("Na", aantal_jaren, "jaar sparen aan een interest van", interest_per_jaar, "% staat er", startbedrag, "euro op de spaarrekening.")
