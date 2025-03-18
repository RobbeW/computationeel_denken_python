zijde = int(input("Geef de zijde van de driehoek in: "))

print("Een gelijkbenige rechthoekige driehoek met benen van", zijde, "bevat deze punten:")
for i in range(zijde):
    for j in range(i + 1):
        print("(", i, ",", j, ")")
