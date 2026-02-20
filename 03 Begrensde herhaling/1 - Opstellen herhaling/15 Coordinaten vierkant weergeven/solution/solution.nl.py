zijde = int(input("Geef de zijde van het vierkant in: "))

print(f"Een vierkant met een zijde van {zijde} punten, bevat deze punten:")
for i in range(zijde):
    for j in range(zijde):
        print(f"( {i} , {j} )")
