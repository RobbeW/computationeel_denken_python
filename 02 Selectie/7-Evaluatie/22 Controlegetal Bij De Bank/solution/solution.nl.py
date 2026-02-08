basisgetal = int(input("Geef de eerste 10 cijfers van het rekeningnummer: "))
controlegetal = int(input("Geef het controlegetal (2 cijfers): "))

rest = basisgetal % 97
if rest == 0:
    rest = 97

if rest == controlegetal:
    print("Het controlegetal klopt. Het nummer is geldig.")
else:
    print("Het controlegetal klopt niet. Het nummer is ongeldig.")
