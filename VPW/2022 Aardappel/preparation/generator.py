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

cases = [([2, 4, 7], 1),
         ([4, 8, 14], 2),
         ([5, 7, 11, 13], 1),
         ([11, 23, 41, 15, 16], 1),
         ([49, 29, 84, 94, 60, 59, 12, 78, 9, 30, 35, 88, 56, 93, 55, 82, 25, 89, 60, 14, 83, 99, 18, 90, 80, 16, 31, 9, 42, 70, 70, 77, 8, 65, 19, 64, 79, 24, 53, 54, 36, 72, 41, 88, 42, 56, 47, 57, 69, 23, 84, 87, 79, 12, 97], 5),
         ([32, 14, 70, 82, 50, 60, 55, 62, 76, 88, 61, 97, 38], 4),
         ([17, 86, 82, 96, 91, 20, 71, 19, 7, 7, 25, 62, 42, 9, 50, 80, 48, 34, 86, 56, 75, 32], 5),
         ([25, 49, 75, 97, 77, 50, 88, 19, 86, 9, 94, 69, 81, 20, 64, 91, 79, 41, 95, 89, 48, 22, 47, 52, 10, 64, 81, 24, 56, 91, 36, 95, 43, 94, 92, 38, 57, 72, 97, 78, 77, 15, 86, 23, 9, 46, 35, 42, 46], 8),
         ([35, 9, 29, 10, 28, 56, 53, 89, 79, 12, 18, 58, 39, 49, 62, 61, 14, 83, 44, 61, 25, 90, 23, 26, 18, 22, 99, 70, 82, 67, 38, 76, 84, 74, 68, 40, 64, 46, 83, 79, 33], 2),
         ([55, 66, 24, 33, 49, 67, 76, 45, 64, 65, 86, 24, 36, 9, 8, 95, 99, 26, 63, 94, 59, 58, 48, 49, 36, 26, 27, 12, 26, 60, 92, 46, 68, 40, 62, 43, 10, 34, 16, 48, 93, 93, 63, 87, 8, 71, 86, 19, 13, 8, 43, 88, 8, 93, 89, 69, 68, 14, 16, 7, 56, 80], 1)
         ]

while len(cases) < ntests:
    n = random.randint(3,100)
    potatos = [random.randint(2,99) for _ in range(n)]
    G = random.randint(1,10)
    
    
    case = (potatos, G)
    if case not in cases:
        cases.append(case)

cases = sorted(cases, key = lambda x: len(x[0]))

# generate unit tests for functions
yamldata = []
tabtitle = "Feedback"

yamldata.append( {'tab': tabtitle, 'contexts': []})

for i in range(len(cases)):
    test = cases[i]

    yamldata[0]['contexts'].append( {'testcases' : []})
       
    # generate test expression
    expression_name = f"aardappel({test[0]}, {test[1]})"
    print(expression_name)
    try:
        outputF = io.StringIO()
        with contextlib.redirect_stdout(outputF):
            result = module.aardappel(test[0], test[1])
        stdout = outputF.getvalue() ##printed value

        print(stdout)
        print(result)
        # setup for return expressions
        testcase = { "expression": expression_name, "return" : result }
        yamldata[0]['contexts'][i]["testcases"].append( testcase)
    except Exception as e:
        print(e)    

write_yaml(yamldata)


