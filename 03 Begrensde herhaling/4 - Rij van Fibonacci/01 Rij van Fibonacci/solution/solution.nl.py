n = int(input("Geef het rangnummer in: ")) 
if n <= 2: 
    print("Het", str(n), "e getal is 1") 
else: 
    voorlaatste = 1 
    voorvoorlaatste = 1 
    for i in range(3, n + 1): 
        nieuw = voorlaatste + voorvoorlaatste 
        voorvoorlaatste = voorlaatste 
        voorlaatste = nieuw 
    print("Het", str(n), "e getal is", nieuw)
