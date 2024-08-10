# standaard uurloon en overuren uurloon
standaard_uurloon = 12
overuren_uurloon = 15

# vraag de gebruiker naar het aantal gewerkte uren
gewerkte_uren = float(input("Hoeveel uur werd er gewerkt? "))

# bereken het verdiende bedrag
if gewerkte_uren <= 8:
    verdiende_bedrag = gewerkte_uren * standaard_uurloon
else:
    verdiende_bedrag = 8 * standaard_uurloon + (gewerkte_uren - 8) * overuren_uurloon

# druk het verdiende bedrag af op het scherm
print()
print("Simon heeft vandaag", round(verdiende_bedrag, 2), "euro verdiend.")
