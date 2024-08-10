import os
import math
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

# generate seed numbers data
cases = [ ]
for i in range(3,15):
    exp = math.ceil(i / 2)
    seed = random.randint(1,100000)
    n = 10**exp
    cases.append( (seed, n ) )


#cases = [ cases_notsorted[0]]
#for i in range(1, len(cases_notsorted)):
#    item = cases_notsorted[i]
#    for j in range(len(cases)):
#        if item[1] <= cases[j][1]:
#            cases.insert(j, item)
#            break 

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
    
    # We doen dit een aantal keer
    for _ in range(n):
        # Genereer twee willekeurige getallen tussen 1 en 6
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        c = random.randint(1, 6)
        d = random.randint(1, 6)
        e = random.randint(1, 6)
        
        m = min(a,b,c,d,e)
        M = max(a,b,c,d,e)
        # Enkel als 
        if (m == 1 and M == 5) or (m == 2 and M == 6):
            # controleren of er geen twee dezelfde tussenzitten
            if not( a == b or a == c or a == d or a == e or b == c or b == d or b == e or c == d or c == e or d == e):
                aantal += 1

    # Bereken het gemiddelde
    kans = round( aantal / n * 100, 2)

    # Print het gemiddelde van de worpen naar het scherm
    outputtxt = f"De kans op grote straat is ongeveer {kans} %\n"
    
    # setup for return expressions
    testcase["input"]["stdin"] = {"type": "text", 
                                  "data": n }
    testcase["output"]["stdout"] = {"type": "text", 
                                    "data": outputtxt }
    

    exportdata["tabs"][0]["contexts"][i]["testcases"].append( testcase )

write_json( exportdata )