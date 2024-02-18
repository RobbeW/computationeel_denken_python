import os
import subprocess
import importlib
import random
import math
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
ntests = 20
cases = [ (123, 5)]

while len( cases ) < ntests:
    seed = random.randint(1,10000)
    n = random.randint(2,20)
    cases.append( (seed, n ) )
    
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
    random.seed(seed)
    
    outputtxt = ""
    bedrag = random.randint(500, 1001)
    aantal_jaren = n
    interest_per_jaar = 2.0

    for j in range (aantal_jaren): 
        outputtxt += 'Na ' + str(j) +' jaar staat er ' +str(round(bedrag, 2))+ ' euro op de rekening.\n'
        bedrag *= ( 1 + interest_per_jaar/100 )

    outputtxt += "Na "+str(aantal_jaren)+" jaar sparen aan een interest van "+str(interest_per_jaar)+ " % staat er "+str(round(bedrag, 2))+ " euro op de spaarrekening.\n"
    
    # setup for return expressions
    testcase["input"]["stdin"] = {"type": "text", 
                                  "data": n }
    testcase["output"]["stdout"] = {"type": "text", 
                                    "data": outputtxt }
    

    exportdata["tabs"][0]["contexts"][i]["testcases"].append( testcase )

write_json( exportdata )