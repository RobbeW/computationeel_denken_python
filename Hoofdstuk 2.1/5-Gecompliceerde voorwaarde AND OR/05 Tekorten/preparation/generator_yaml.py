import os
import random
import ruamel.yaml
import subprocess

yaml = ruamel.yaml.YAML()

# set fixed seed for generating test cases
random.seed( 123456789 )

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join('..', 'solution')
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

# load functionality defined in sample solution
module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.nl.py')


def write_yaml( data:list ):
    """ A function to write YAML file"""
    with open(os.path.join('..', 'evaluation', 'tests.yaml'), 'w', encoding='utf-8') as f:
        yaml.dump(data, f)

# generate test data
ntests= 30
cases = [ (55,48), (81,76), (33,48), (50,53),(50,50),(50,49) ]

while len( cases ) < ntests:
    case = (random.randint(0,99) for _ in range(2))
    
    cases.append( case )

# generate unit tests for functions
yamldata = []
yamldata.append( {'tab': 'Feedback', 'testcases': []})
# input, expression, statement or stdin?
input = 'stdin'
# output, stdout or return?
output = 'stdout'
for test in cases:
    # generate test expression
    expression_name = '\n'.join(map(str, test))
    
    # generate output to output file
    script = os.path.join(solutiondir, 'solution.nl.py')
    process= subprocess.run(
        ['python3', script],
        input = expression_name,
        encoding = 'utf-8',
        capture_output = True,
        universal_newlines = True
    )
    
    result = ""
    
    result_lines = process.stdout.split("\n")
    for i in range(1,len(result_lines)-1):
        print(result_lines[i])
        result += result_lines[i]
    
    # setup for return expressions
    testcase = { input: expression_name, output: result }
    yamldata[0]['testcases'].append( testcase )

write_yaml(yamldata)