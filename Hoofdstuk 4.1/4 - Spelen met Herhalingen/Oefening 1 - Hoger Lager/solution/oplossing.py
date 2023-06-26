import random

# Startscore
score = 0

# Genereer twee willekeurige getallen
getal_1 = random.randint(1, 10)
getal_2 = random.randint(1, 10)

# We maken een variable aan zodat we blijven spelen: 
spelen = True


while spelen == True:
    # Genereer twee nieuwe getallen
    getal_1 = random.randint(1, 10)
    getal_2 = random.randint(1, 10)
    
    while getal_1 == getal_2:
        getal_2 = random.randint(1, 10)
        
    # Toon het eerste getal en vraag om een voorspelling
    print("Getal 1 is:", getal_1)
    voorspelling = input("Is getal 2 hoger of lager? ")
    
    if (voorspelling == "hoger" and getal_2 > getal_1) or (voorspelling == "lager" and getal_2 < getal_1):
        # Verhoog de score
        score += 1
    
    else: 
        spelen = False


# Als de voorspelling niet correct is
print("GAME OVER")
print("Jouw score is", score)
