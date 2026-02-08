import math

diameter_a = float(input("Voer de diameter van reactievat A in: "))
hoogte_a = float(input("Voer de hoogte van reactievat A in: "))

diameter_b = float(input("Voer de diameter van reactievat B in: "))
hoogte_b = float(input("Voer de hoogte van reactievat B in: "))

straal_a = diameter_a / 2
straal_b = diameter_b / 2

volume_a = math.pi * (straal_a ** 2) * hoogte_a
volume_b = math.pi * (straal_b ** 2) * hoogte_b

volume_a = round(volume_a, 2)
volume_b = round(volume_b, 2)

print("Volume reactievat A:", volume_a,"m³.")
print("Volume reactievat B:", volume_b,"m³.")

if volume_a > volume_b:
    print("Reactievat A heeft het grootste volume.")
elif volume_b > volume_a:
    print("Reactievat B heeft het grootste volume.")
else:
    print("Reactievat A en B hebben een gelijk volume.")
