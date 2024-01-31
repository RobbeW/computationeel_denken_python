# Vraag de gebruiker om het startgetal, startexponent en eindexponent
startgetal = int(input("Voer een startgetal in: "))
startexponent = int(input("Voer een startexponent in: "))
eindexponent = int(input("Voer een eindexponent in: "))

# Print het startgetal
print("Gekozen startgetal: " + str(startgetal))

# Itereer over de exponenten van startexponent tot en met eindexponent
for exponent in range(startexponent, eindexponent + 1):
    resultaat = startgetal ** exponent
    print(startgetal, "tot de macht", exponent, "is:", resultaat)
