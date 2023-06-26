fibonacci = [0, 1]
for i in range (2, 101): 
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
#print(fibonacci)

vraag = int(input("Voer het getal in van de Fibonacci-reeks dat u wilt zien (tussen 1 en 100): "))

print('Getal nummer ', vraag, ' in de Fibonacci-reeks is ', fibonacci[vraag])