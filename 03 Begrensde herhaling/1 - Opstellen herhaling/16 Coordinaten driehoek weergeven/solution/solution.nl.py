zijde = int(input("Geef de zijde van de driehoek in: "))

print(f"Een gelijkbenige rechthoekige driehoek met {zijde} punten op de benen, bevat deze punten:")
for i in range(zijde):
    for j in range(zijde - i):
        print(f"( {i} , {j} )")
