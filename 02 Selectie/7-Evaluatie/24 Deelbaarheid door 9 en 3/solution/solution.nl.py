getal = int(input("Voer een geheel getal van exact vier cijfers in:"))

D = getal // 1000
rest = getal % 1000

H = rest // 100
rest = rest % 100

T = rest // 10
E = rest % 10

som = D + H + T + E

if getal % 9 == 0:
    print("Het getal is deelbaar door 3 en 9.")
    print("Dit kan je controleren door: " + str(D) + ", " + str(H) + ", " + str(T) + " en " + str(E) + " op te tellen, zo bekom je " + str(som) + ".")
    print("Deze som is deelbaar door 3 en 9.")
elif getal % 3 == 0:
    print("Het getal is deelbaar door 3 en niet door 9.")
    print("Dit kan je controleren door: " + str(D) + ", " + str(H) + ", " + str(T) + " en " + str(E) + " op te tellen, zo bekom je " + str(som) + ".")
    print("Deze som is deelbaar door 3.")
else:
    print("Het getal is niet deelbaar door 9 en 3.")
    print("Dit kan je controleren door: " + str(D) + ", " + str(H) + ", " + str(T) + " en " + str(E) + " op te tellen, zo bekom je " + str(som) + ".")
    print("Deze som is niet deelbaar door 9, noch door 3.")
