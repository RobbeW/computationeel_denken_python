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
ntests = 1
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
     
    # generate test expression        
    testcase = {"description": "Uitvoeren met seed "+str(seed)+" leidt tot:",
                "input": {},
                "output": {} }
    
    # PROGRAM IMPLEMENTATION
    random.seed(seed) #setting the seed
    score = 0
    outputtxt = ""
    inputtxt = ""
    numbers = []
    for _ in range(5):
        numbers.append( tuple(random.randint(1, 10) for _ in range(2)) )
    
    for nums in numbers:
        num1 = nums[0]
        num2 = nums[1]
        outputtxt += "Getal 1: "+str(num1)+"\nGetal 2: "+str(num2)+"\n"
        
        if random.randint(0,1):
            product = num1*num2
            inputtxt += str(product)+"\n"
            outputtxt += "Goed zo!\n"
            score += 1
        else:
            product = num1*num2
            fout = product + (-1)**random.randint(1,2)*random.randint(1,5)
            inputtxt += str(fout)+"\n"
            outputtxt += "Dat is niet correct. Het juiste antwoord is "+str(product)+"\n"
        
    outputtxt += "Je totaalscore is "+str(score)+" op 5.\n"


    # fill in the testcase
    testcase["input"]["stdin"] = {"type": "text", 
                                  "data": inputtxt }
    testcase["output"]["stdout"] = {"type": "text", 
                                    "data": outputtxt }
    

    exportdata["tabs"][0]["contexts"][i]["testcases"].append( testcase )

write_json( exportdata )