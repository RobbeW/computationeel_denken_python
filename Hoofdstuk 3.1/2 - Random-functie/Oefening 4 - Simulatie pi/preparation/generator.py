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
ntests = 10
cases = [ (123, 100000)]

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
    random.seed(seed)
    aantal = 0
    
    for _ in range(n):
        x = random.randint(-100, 100) / 100
        y = random.randint(-100, 100) / 100
        
        if math.sqrt(x**2+y**2) < 1:
            aantal += 1

    schatting = round( 4 * aantal / n, 5)
    outputtxt = "Bij "+ str(n)+ " simulaties bedraagt de schatting voor pi ongeveer: "+str(schatting)
    
    # setup for return expressions
    testcase["input"]["stdin"] = {"type": "text", 
                                  "data": n }
    testcase["output"]["stdout"] = {"type": "text", 
                                    "data": outputtxt }
    

    exportdata["tabs"][0]["contexts"][i]["testcases"].append( testcase )

write_json( exportdata )