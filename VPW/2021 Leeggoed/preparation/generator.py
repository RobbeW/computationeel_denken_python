import os
import importlib.util
import random
import ruamel.yaml
import contextlib, io

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
spec.loader.exec_module(module)

# generate test data
ntests = 25

cases = [(2, 2, 3),
         (7, 1, 8),
         (50, 2, 4),
         (227, 38, 41),
         (142, 51, 63),
         (504, 25, 43),
         (982, 59, 71),
         (101, 79, 80)
         ]

while len(cases) < ntests:
    aantal = random.randint(0, 200)
    prijs_vol = random.randint(2, 100)
    prijs_leeg = random.randint(1, prijs_vol - 1)
    
    
    case = (aantal, prijs_leeg, prijs_vol)
    if case not in cases:
        cases.append(case)

cases = sorted(cases, key = lambda x: x[0])

# generate unit tests for functions
yamldata = []
tabtitle = "Feedback"

yamldata.append( {'tab': tabtitle, 'contexts': []})

for i in range(len(cases)):
    test = cases[i]

    yamldata[0]['contexts'].append( {'testcases' : []})
       
    # generate test expression
    expression_name = f"leeggoed({test[0]}, {test[1]}, {test[2]})"
    print(expression_name)
    try:
        outputF = io.StringIO()
        with contextlib.redirect_stdout(outputF):
            result = module.leeggoed(test[0], test[1], test[2])
        stdout = outputF.getvalue() ##printed value

        print(stdout)
        print(result)
        # setup for return expressions
        testcase = { "expression": expression_name, "return" : result }
        yamldata[0]['contexts'][i]["testcases"].append( testcase)
    except Exception as e:
        print(e)    

write_yaml(yamldata)


