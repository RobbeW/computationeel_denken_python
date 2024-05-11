import random

flag = True
speler1 = 0
while flag:
    a = random.randint(1,6)
    b = random.randint(1,6)
    speler1 += 1
    flag = not (a == 6 == b)
    
flag = True
speler2 = 0
while flag:
    a = random.randint(1,6)
    b = random.randint(1,6)
    speler2 += 1
    flag = not (a == 6 == b)
    
if speler1 < speler2:
    print("Speler 1 wint!")
elif speler1 > speler2:
    print("Speler 2 wint!")
else:
    print("Gelijkstand.")
