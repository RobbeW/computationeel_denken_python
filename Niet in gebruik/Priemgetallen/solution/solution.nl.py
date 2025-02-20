def is_priem(getal):
    i = 2
    while i < getal and getal % i != 0:
        i = i + 1
    # Indien geen delers werden gevonden is i == getal
    return i == getal

get = int(input())
if is_priem(get):
    print('Y')
else:
    print('N')