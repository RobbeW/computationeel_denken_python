# generate test data
import os
import sys
import importlib.util
import random
import ruamel.yaml
import subprocess

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
ntests= 20
belgian_names = [
    ("Lucas", "Dupont"),
    ("Emma", "De Smet"),
    ("Noah", "Dubois"),
    ("Léa", "Mertens"),
    ("Liam", "Wouters"),
    ("Marie", "Jacobs"),
    ("Arthur", "Lemmens"),
    ("Julie", "Goossens"),
    ("Louis", "Dumont"),
    ("Zoé", "Simons"),
    ("Victor", "Vanderlinden"),
    ("Sarah", "Nys"),
    ("Gabriel", "Van den Bossche"),
    ("Clara", "Smets"),
    ("Hugo", "Dewitte"),
    ("Alice", "Hendrickx"),
    ("Thomas", "Rousseau"),
    ("Laura", "De Greef"),
    ("Nathan", "Thys"),
    ("Elise", "Vandenberghe"),
    ("Milan", "Sleurs"),
    ("Chloé", "Geerts"),
    ("Jules", "Michiels"),
    ("Charlotte", "Vandamme"),
    ("Maxime", "Roels"),
    ("Lena", "Van den Heuvel"),
    ("Axel", "Coenen"),
    ("Lina", "Vandersteen"),
    ("Alexandre", "Verleyen"),
    ("Manon", "Luyten")
]

cases = [("Mathieu", "De Baets", "Rufus", "Morael")]
while len(cases) < ntests:
    pers1 = random.choice(belgian_names)
    pers2 = random.choice(belgian_names)
    if pers1 != pers2 and (pers1[0], pers1[1], pers2[0], pers2[1]) not in cases:
        cases.append( (pers1[0], pers1[1], pers2[0], pers2[1]) )

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
        ['python3', script],
        input=stdin,
        encoding='utf-8',
        capture_output=True
    )
    
    result_lines = process.stdout.split("\n")
    result_lines = [x for x in result_lines[:-1]] ## drop last element
    
    outputtxt = ""
    for line in result_lines:
        if not(line.startswith( 'Geef' ) or line.startswith( 'Voer' )):
            print(line)
            outputtxt += line + "\n"
            
    testcase = { input: stdin, output: outputtxt }            
    yamldata[0]['contexts'][i]["testcases"].append( testcase)


write_yaml(yamldata)