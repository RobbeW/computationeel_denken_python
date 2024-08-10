import random

woorden = open('../workdir/words.txt').read().split("\n")
woord = random.choice(woorden)

aantal_correct = 0
aantal_tekens = 8
aantal_gokken = 0
tekens = "????????"
while aantal_correct < aantal_tekens and aantal_gokken < 10:
    print(tekens)
    gok = input("Gok een letter: ")
    
    correct = False
    if gok not in tekens:
        for i in range(8):
            letter = woord[i]
            if gok == letter:
                aantal_correct += 1
                correct = True
                
                tijdelijk = list(tekens)
                tijdelijk[i] = gok
                tekens = "".join(tijdelijk)
        
    if correct == False:
        aantal_gokken += 1
        print(letter, "werd niet gevonden")

if aantal_correct == 8:
    print(tekens)
    print("Je hebt het woord gevonden!")
else:
    print("Het woord was", woord)