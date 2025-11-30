# Vraag een geheel getal:
getal = int(input("Geef een geheel getal in: "))

# Controleer of het getal in het juiste interval ligt:
if getal <= 0:
    print("Ongeldige invoer: het getal moet groter zijn dan 0.")
elif getal >= 1000:
    print("Ongeldige invoer: het getal moet kleiner zijn dan 1000.")
else:
    H = getal // 100
    T = (getal // 10) % 10
    E = getal % 10

    # Bereken het verschil:
    verschil = getal - (H + T + E)

    # Weergave H, T en E:
    regel = "Honderdtallen: " + str(H) + ", Tientallen: " + str(T) + ", Eenheden: " + str(E)
    print(regel)

    # Weergave van het verschil:
    print("Verschil =", verschil)

    # Controleer of het verschil deelbaar is door 9: 
    if verschil % 9 == 0:
        print(verschil, "is deelbaar door 9.")
    else:
        print(verschil, "is niet deelbaar door 9.")
