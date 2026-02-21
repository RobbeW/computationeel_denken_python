n = int(input("Geef het rangnummer in: ")) 

nieuw = 1

voorlaatste = 1 
voorvoorlaatste = 1 
for i in range(n - 1): 
    nieuw = voorlaatste + voorvoorlaatste 
    voorvoorlaatste = voorlaatste 
    voorlaatste = nieuw 

print(f"Het getal uit de rij van Fibonacci met rangnummer {n} is {nieuw}")
