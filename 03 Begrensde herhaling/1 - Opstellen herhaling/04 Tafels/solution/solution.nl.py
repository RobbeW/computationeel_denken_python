# Vraag een grondtal
getal = int( input( "Geef een getal in: " ) )

# Gebruik een for-lus om de tafel weer te geven
for i in range(1, 11):  # de range-functie genereert getallen van 1 tot 10
    product = i * getal  # bereken het product van i en het getal
    print(i, "x", getal,"=", product)  # print het product op het scherm
