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
ntests = 5
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
    exportdata["tabs"][0]["contexts"][i]["before"] = []
    exportdata["tabs"][0]["contexts"][i]["testcases"] = []
    
    seed = test[0]
    # generate before expression
    beforecase = {"python": {"data": "import random; random.seed("+str(seed)+")"}}
    exportdata["tabs"][0]["contexts"][i]["before"].append(beforecase)
     
    # generate test expression        
    testcase = {"description": "Uitvoeren met seed "+str(seed)+" leidt tot:",
                "output": {} }
    
    # generate output to output file
    script = os.path.join(solutiondir, 'solution.nl.py')
    process= subprocess.run(
        ['python3', script],
        encoding='utf-8',
        capture_output=True,
        text=True
    )

    result = process.stdout

    # setup for return expressions
    testcase["output"]["stdout"] = {"type": "text", 
                                    "data": result }
    

    exportdata["tabs"][0]["contexts"][i]["testcases"].append( testcase )

write_json( exportdata )