zijde = int(input("Geef de zijde van het vierkant in: "))

print()
print("Een vierkant met een zijde van", zijde, "bevat deze punten:")
for i in range(zijde):
    for j in range(zijde):
        print("(", i, ",", j, ")")
