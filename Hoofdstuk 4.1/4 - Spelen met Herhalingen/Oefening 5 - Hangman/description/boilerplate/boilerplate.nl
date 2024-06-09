import random
import urllib3

# Dit stukje code leest een willekeurig woord van 8 tekens in
target_url = "https://tinyurl.com/2dfecxkz"

http = urllib3.PoolManager()
response = http.request('GET', target_url)
woorden = response.data.decode('utf-8').split("\n")
woord = random.choice(woorden)

# Hieronder komt je de rest van je programma
tekens = "????????"   # Gebruik deze variabele 

