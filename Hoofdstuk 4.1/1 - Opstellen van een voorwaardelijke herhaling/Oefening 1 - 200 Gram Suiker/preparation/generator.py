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
ntests = 10
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
    
    outputtxt = ""
    # PROGRAM IMPLEMENTATION
    random.seed(seed) #setting the seed
    
    potje = 0 
    aantal = 0
    while potje < 200:
        aantal += 1
        potje += random.randint(110, 150)/10
        outputtxt += f"Na {aantal} lepels, heeft Laura {round(potje, 1)} g suiker.\n"

    # generate test expression
    testcase = {"description": "Uitvoeren met seed "+str(seed)+" leidt tot het onderstaande",
                "output": {} }

    # fill in the testcase
    testcase["output"]["stdout"] = {"type": "text", 
                                    "data": outputtxt }
    

    exportdata["tabs"][0]["contexts"][i]["testcases"].append( testcase )

write_json( exportdata )