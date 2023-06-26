# Gebruik een for-lus om de tafel van 7 af te drukken tot '10 x 7'
for i in range(1, 11):  # de range-functie genereert getallen van 1 tot 10
    product = i * 7  # bereken het product van het huidige getal en 7
    print(i, "x 7 =", product)  # print het product op het scherm