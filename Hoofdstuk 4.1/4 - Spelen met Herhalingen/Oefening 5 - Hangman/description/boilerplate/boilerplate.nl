import random

# Dit stukje code leest een willekeurig woord van 8 tekens in
# Dit is een stukje voor de "Sandbox"
import urllib3
target_url = "https://tinyurl.com/2dfecxkz"

http = urllib3.PoolManager()
response = http.request('GET', target_url)
woorden = response.data.decode('utf-8').split("\n")
woord = random.choice(woorden)

# Dit is een stukje voor het indienen in Dodona
#woorden = open('../workdir/words.txt').read().split("\n")
#woord = random.choice(woorden)

# Hieronder komt je de rest van je programma
tekens = "????????"   # Gebruik deze variabele 

