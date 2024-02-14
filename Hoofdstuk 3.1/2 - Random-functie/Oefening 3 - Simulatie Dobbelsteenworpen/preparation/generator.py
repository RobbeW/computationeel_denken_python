import os
import subprocess
import importlib
import random
import json

# set fixed seed for generating test cases
random.seed(123456789)

# locate evaldir
evaldir = os.path.join("..", "evaluation")
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join("..", "solution")
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

def write_json( data:dict ):
    """ A function to write JSON file"""
    with open(os.path.join("..", "evaluation", "tests.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent = 2)

# generate test data
ntests = 10
cases = [ ]

while len( cases ) < ntests:
    seed = random.randint(1,10000)
    n = 10**random.randint(1,7) *0.5**random.randint(0,1)
    cases.append( (seed, int(n) ) )
    
# generate unit tests for functions
exportdata = {"tabs": [] }
exportdata["tabs"].append( {"name": "Feedback",
                            "contexts": [] } )

i = -1

for test in cases:
    exportdata["tabs"][0]["contexts"].append({})
    i += 1    
    seed = test[0]
    n = test[1]
    # generate before expression
    beforecase = {"python": {"data": "import random; random.seed("+str(seed)+")"}}
    exportdata["tabs"][0]["contexts"][i]["before"] = beforecase
     
    exportdata["tabs"][0]["contexts"][i]["testcases"] = []
    
    # generate test expression        
    testcase = {"description": "Uitvoeren met seed "+str(seed)+" en invoer "+ str(n) +" leidt tot:",
                "input": {},
                "output": {} }
    
    # generate output to output file
    som = 0
    random.seed(seed)
    for _ in range(n):
        worp1 = random.randint(1, 6)
        worp2 = random.randint(1, 6)
        
        som += worp1 + worp2

    gemiddelde = round( som / n, 2)

    # Print het gemiddelde van de worpen naar het scherm
    outputtxt = "Het gemiddelde bij " + str(n) +" worpen is "+ str(gemiddelde)+"\n"
    
    # setup for return expressions
    testcase["input"]["stdin"] = {"type": "text", 
                                  "data": n }
    testcase["output"]["stdout"] = {"type": "text", 
                                    "data": outputtxt }
    

    exportdata["tabs"][0]["contexts"][i]["testcases"].append( testcase )

write_json( exportdata )