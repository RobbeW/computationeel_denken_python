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
ntests = 20

kinds = ["♠", "♥", "♣", "♦"]
symb = ["B", "9", "A", "T", "H", "D", "8", "7"]
cards = []
for kind in kinds:
    for sym in symb:
        cards.append(kind + sym)

cases = [("♠", ["♦B", "♦7", "♠9", "♠7", "♥D", "♥7", "♣B", "♣7"]),
         ("♥", ["♦B", "♦7", "♠9", "♠7", "♥D", "♥7", "♣B", "♣7"])]

while len(cases) < ntests:
    kaarten = random.sample(cards, k = 8)
    troef = kaarten[0][0]
    case = (troef, kaarten)
    if case not in cases:
        cases.append(case)

# generate unit tests for functions
yamldata = []
tabtitle = "Feedback"

yamldata.append( {'tab': tabtitle, 'contexts': []})

for i in range(len(cases)):
    test = cases[i]

    yamldata[0]['contexts'].append( {'testcases' : []})
       
    # generate test expression
    expression_name = f"klaverjassen(\"{test[0]}\", {test[1]})"
    print(expression_name)
    try:
        outputF = io.StringIO()
        with contextlib.redirect_stdout(outputF):
            result = module.klaverjassen(test[0], test[1])
        stdout = outputF.getvalue() ##printed value

        print(stdout)
        print(result)
        # setup for return expressions
        testcase = { "expression": expression_name, "return" : result }
        yamldata[0]['contexts'][i]["testcases"].append( testcase)
    except Exception as e:
        print(e)    

write_yaml(yamldata)


