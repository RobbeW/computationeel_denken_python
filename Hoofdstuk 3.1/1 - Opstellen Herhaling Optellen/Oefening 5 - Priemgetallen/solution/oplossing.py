print("De priemgetallen kleiner dan 100 zijn:")
print(1)
# Ga door de getallen van 2 tot 99
for i in range(2, 100):
    # Stel in dat het getal een priemgetal is tot het tegendeel bewezen is
    priemgetal = True
    
    # Probeer het getal te delen door elk getal kleiner dan zichzelf en groter dan 1
    for j in range(2, i):
        if i % j == 0:
            # Als het getal gedeeld kan worden, is het geen priemgetal
            priemgetal = False
            break
    
    # Als er geen delers gevonden werden, print dan het getal op het scherm
    if priemgetal == True:
        print(i)
