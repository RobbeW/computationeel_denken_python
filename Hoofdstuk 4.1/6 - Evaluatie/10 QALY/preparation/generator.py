import os
import sys
import importlib
import random
import ruamel.yaml
import subprocess
import numpy as np

yaml = ruamel.yaml.YAML()

# set fixed seed for generating test cases
random.seed(12345678)

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join('..', 'solution')
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

def write_yaml( data:list ):
    """ A function to write YAML file"""
    with open(os.path.join('..', 'evaluation', 'tests.yaml'), 'w', encoding='utf-8') as f:
        yaml.dump(data, f)


module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.nl.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
#spec.loader.exec_module(module)

# generate test data
ntests = 50
cases = [(5,12.0,1.0,5.2,0.7,10.7,0.9,20.4,0.5,30.0,0.2), (1,3.2,0.4)]

while len( cases ) < ntests:
    n = np.random.binomial(10,0.35)**2 + random.randint(0,5)
    list = [random.randint(1,100) for _ in range(n)]
    som = sum(list)
    # normaliseren en omvormen naar een max leeftijd:
    maxl = round(random.uniform(40,100), 1)
    case = [n]
    for a in list:
        age = round( a / som * maxl, 1 )
        case.append(age)
        q = round(random.randint(1,10) / 10, 1)
        case.append(q)
    if n > 0:
        cases.append(tuple(case))
        
    
# generate unit tests for functions
yamldata = []

# input, expression, statement or stdin?
input = 'stdin'
# output, stdout or return?
output = 'stdout'
tabtitle = "Feedback"

yamldata.append( {'tab': tabtitle, 'contexts': []})

for i in range(len(cases)):
    test = cases[i]
    yamldata[0]['contexts'].append( {'testcases' : []})
    # generate test expression
    # add input to input file
    stdin = '\n'.join(f'{line}' for line in test)

    # generate output to output file
    script = os.path.join(solutiondir, 'solution.nl.py')
    process= subprocess.run(
        ['python3.8', script],
        input=stdin,
        encoding='utf-8',
        capture_output=True
    )
    
    result_lines = process.stdout.split("\n")
    result_lines = [x for x in result_lines[:-1]] ## drop last element
    

    outputtxt = ""
    for line in result_lines:
        if not(line.startswith( 'Geef' )):
            print(line)
            outputtxt += line + "\n"
            
    testcase = { input: stdin, output: outputtxt }            
    yamldata[0]['contexts'][i]["testcases"].append( testcase)


write_yaml(yamldata)