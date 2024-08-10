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
    
    # PROGRAM IMPLEMENTATION
    random.seed(seed) #setting the seed
    
    flag = True
    speler1 = 0
    while flag:
        a = random.randint(1,6)
        b = random.randint(1,6)
        speler1 += 1
        flag = not (a == 6 == b)
        
    flag = True
    speler2 = 0
    while flag:
        a = random.randint(1,6)
        b = random.randint(1,6)
        speler2 += 1
        flag = not (a == 6 == b)
        
    outputtxt = f"Aantal worpen speler 1: {speler1}\n"
    outputtxt += f"Aantal worpen speler 2: {speler2}\n"
    if speler1 < speler2:
        outputtxt += "Speler 1 wint!\n"
    elif speler1 > speler2:
        outputtxt += "Speler 2 wint!\n"
    else:
        outputtxt += "Gelijkstand.\n"
    
    # generate test expression

    testcase = {"description": "Uitvoeren met seed "+str(seed)+" leidt tot het onderstaande",
                "input": {},
                "output": {} }

    # fill in the testcase
    testcase["input"]["stdin"] = "none"
    testcase["output"]["stdout"] = {"type": "text", 
                                    "data": outputtxt }
    

    exportdata["tabs"][0]["contexts"][i]["testcases"].append( testcase )

write_json( exportdata )