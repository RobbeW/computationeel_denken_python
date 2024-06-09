import random

opties = ["blad", "steen", "schaar"]

voorwaarde = True
score = 0
totaal = 0
while voorwaarde:
    computer = random.choice(opties)
    gok = input("Geef een optie in, of stop: ")
    if gok != "stop":
        totaal += 1
        print("De computer koos", computer)
        if gok == "blad" and computer == "steen":
            score += 2
            print("Je wint!")
        elif gok == "steen" and computer == "schaar":
            score += 2
            print("Je wint!")
        elif gok == "schaar" and computer == "papier":
            score += 2
            print("Je wint!")
        elif gok == computer:
            score += 1
            print("Gelijkspel!")
        else:
            print("Je verliest!")
    else:
        voorwaarde = False

print("Je score was", score, "op", 2 * totaal)