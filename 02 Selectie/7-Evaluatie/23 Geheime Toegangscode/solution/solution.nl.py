code = int(input("Voer de code in: "))

if code % 4 == 0 and code % 6 == 0:
    print("Toegang verleend: Hoofdsysteem ontgrendeld!")
elif code % 4 == 0 or code % 6 == 0:
    print("Bijna goed: De eerste deur is geopend.")
else:
    print("Toegang geweigerd!")
