# Laat deze code staan
invoer = input("Geef de RGB waarden in, gescheiden door een spatie: ")
RGB_waarde = list(map(int, invoer.split()))

# Schrijf hieronder je programmma
RGB_comp = [ 255 - RGB_waarde[0], 255 - RGB_waarde[1], 255 - RGB_waarde[2] ]
print()
print( "De complementaire kleurcode is:", RGB_comp)
