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
opties = ["blad", "steen", "schaar"]
gokken = []

while len( cases ) < ntests:
    seed = random.randint(1,10000)
    cases.append( (seed,) )
    n = (random.randint(0,9)!= 0) * random.randint(1,10)
    gokjes = random.choices(opties, k = n)
    gokjes.append("stop")
    gokken.append(gokjes)
    print(gokjes)
    
    
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
    outputtxt = ""
    inputtxt = ""
    random.seed(seed) #setting the seed
    


    voorwaarde = True
    score = 0
    totaal = 0
    k = 0
    while voorwaarde:
        computer = random.choice(opties)
        gok = gokken[i][k]
        k+=1
        
        inputtxt += gok+"\n"
        if gok != "stop":
            totaal += 1
            outputtxt += f"De computer koos: {computer}\n"
            if gok == "blad" and computer == "steen":
                score += 2
                outputtxt += f"Je wint!\n"
            elif gok == "steen" and computer == "schaar":
                score += 2
                outputtxt += f"Je wint!\n"
            elif gok == "schaar" and computer == "blad":
                score += 2
                outputtxt += f"Je wint!\n"
            elif gok == computer:
                score += 1
                outputtxt += f"Gelijkspel!\n"
            else:
                outputtxt += f"Je verliest!\n"
        else:
            voorwaarde = False

    outputtxt += f"Je score was {score} op {2 * totaal}\n"
    
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