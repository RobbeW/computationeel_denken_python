# Buitenste lus voor de tafels van vermenigvuldiging
for i in range(1, 11):
    print("Tafel van", i, ":")
    
    # Binnenste lus voor de vermenigvuldiger
    for j in range(1, 11):
        # Bereken het product en print de berekening op het scherm
        product = i * j
        print(i, "x", j, "=", product)
