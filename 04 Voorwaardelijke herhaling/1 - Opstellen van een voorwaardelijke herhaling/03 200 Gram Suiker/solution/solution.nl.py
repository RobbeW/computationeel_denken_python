import random

potje = 0 
aantal = 0
while potje < 200:
    aantal += 1
    potje += random.randint(110, 150)/10
    print("Na", aantal, "lepels, heeft Laura", round(potje, 1), 'g suiker.')
