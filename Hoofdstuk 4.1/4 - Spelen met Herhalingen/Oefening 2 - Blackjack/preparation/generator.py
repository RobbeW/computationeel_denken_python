import os
import random
import json

# set fixed seed for generating test cases
random.seed(123456789)

# locate evaldir
evaldir = os.path.join("..", "evaluation")
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

def write_json( data:dict ):
    """ A function to write JSON file"""
    with open(os.path.join("..", "evaluation", "tests.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent = 2)

# generate test data
ntests = 20
cases = [ ]

while len( cases ) < ntests:
    seed = random.randint(1,10000)
    cases.append( (seed,) )
    
# generate unit tests for functions
exportdata = {"tabs": [] }
exportdata["tabs"].append( {"name": "Feedback",
                            "contexts": [] } )

i = -1

for test in cases:
    exportdata["tabs"][0]["contexts"].append({})
    i += 1
        
    seed = test[0]
    # generate before expression
    beforecase = {"python": {"data": "import random; random.seed("+str(seed)+")"}}
    exportdata["tabs"][0]["contexts"][i]["before"] = beforecase
    
    exportdata["tabs"][0]["contexts"][i]["testcases"] = []
    
    choices = random.choices(["ja", "nee"], k = 6)
    j = 0
    
    # PROGRAM IMPLEMENTATION
    random.seed(seed) #setting the seed
    
    kaart_1 = random.randint(1, 10)
    kaart_2 = random.randint(1, 10)
    outputtxt = f"Je kreeg kaarten {kaart_1} en {kaart_2}\n"

    # Bereken de som van de twee getallen
    som = kaart_1 + kaart_2

    # Vraag of de gebruiker nog een kaart wil
    if som >= 19:
        keuze = choices[j]
    else:
        keuze = "ja"
    inputtxt = keuze+"\n"

    # Zolang de gebruiker een kaart wil en de som niet groter is dan 21
    while keuze == 'ja' and som <= 21:
        j +=1
        # Genereer een nieuwe kaart en verhoog de som
        nieuwe_kaart = random.randint(1, 10)
        som += nieuwe_kaart

        # Print de nieuwe kaart en de huidige som
        outputtxt += f"De nieuwe kaart is: {nieuwe_kaart}\n"
        outputtxt += f"De som bedraagt nu: {som}\n"

        # Als de som nog steeds niet groter is dan 21, vraag of de gebruiker nog een kaart wil
        if som < 21:
            if som >= 19:
                keuze = choices[j]
            else:
                keuze = "ja"
            inputtxt += keuze+"\n"
        elif som == 21:
            keuze = "nee"
            inputtxt += keuze+"\n"

    # Als het spel is afgelopen
    if som == 19:
        outputtxt += "Je wint 2 euro!\n"
    elif som == 20:
        outputtxt += "Je wint 5 euro!\n"
    elif som == 21:
        outputtxt += "Je wint 10 euro!\n"
    else:
        outputtxt += "Je verliest!\n"   
    
    # generate test expression
    inputdescr = str.replace(inputtxt, "\n", " - ")  
    testcase = {"description": "Uitvoeren met seed "+str(seed)+" leidt tot het onderstaande (met als achtereenvolgende invoer "+inputdescr[:-3]+")",
                "input": {},
                "output": {} }

    # fill in the testcase
    testcase["input"]["stdin"] = {"type": "text", 
                                  "data": inputtxt }
    testcase["output"]["stdout"] = {"type": "text", 
                                    "data": outputtxt }
    

    exportdata["tabs"][0]["contexts"][i]["testcases"].append( testcase )

write_json( exportdata )