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
       
    # PROGRAM IMPLEMENTATION
    random.seed(seed) #setting the seed
    score = 0
    outputtxt = ""
    inputtxt = ""
    numbers = []
    for _ in range(10):
        numbers.append( tuple(random.randint(1, 20) for _ in range(1)) )
    
    for nums in numbers:
        num1 = nums[0]
        outputtxt += "Zoek het kwadraat van "+str(num1)+"\n"
        
        if random.randint(0,2) != 0:
            product = num1**2
            inputtxt += str(product)+"\n"
            outputtxt += "Goed zo!\n"
            score += 1
        else:
            product = num1**2
            if random.randint(0,1):
                fout = product + (-1)**random.randint(0,1)*random.randint(1,num1)
            else:
                fout = 2*num1
            inputtxt += str(fout)+"\n"
            outputtxt += "Fout, "+ str(product)+ " is het juiste antwoord!\n"
        
    outputtxt += "Je totaalscore is: "+str(score)+" / 10.\n"
    
    
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