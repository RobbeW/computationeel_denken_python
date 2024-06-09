import random

# Dit laat de computer een willekeurig woord uit een grote lijst kiezen
woorden = open('words.txt').read().split("\n")
woord = random.choice(woorden)

# Hieronder komt je programma
tekens = "????????"   # Gebruik deze variabele 
