import os
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

# thnx chatgpt
cases = [
    ("jazzzangeres", 'z'),  # 'z' komt 3 keer voor
    ("lettergreep", 'e'),   # 'e' komt 3 keer voor
    ("voorstel", 'o'),      # 'o' komt 2 keer voor
    ("schrijfster", 'r'),   # 'r' komt 2 keer voor
    ("commissie", 'i'),     # 'i' komt 3 keer voor
    ("appelleer", 'e'),     # 'e' komt 3 keer voor
    ("natuurlijk", 't'),    # 't' komt 2 keer voor
    ("schaduw", 'd'),       # 'd' komt 2 keer voor
    ("herstellingswerkzaamheden", 'e'),  # 'e' komt 5 keer voor
    ("sneeuwvlok", 'n'),    # 'n' komt 2 keer voor
    ("koffiepot", 'o'),     # 'o' komt 2 keer voor
    ("autoweg", 'a'),       # 'a' komt 2 keer voor
    ("roestvrij", 'r'),     # 'r' komt 2 keer voor
    ("papegaaien", 'a'),    # 'a' komt 3 keer voor
    ("schrijver", 'r'),     # 'r' komt 2 keer voor
    ("informatie", 'i'),    # 'i' komt 3 keer voor
    ("boekenkast", 'k'),    # 'k' komt 2 keer voor
    ("verjaardag", 'a'),    # 'a' komt 3 keer voor
    ("computer", 't'),      # 't' komt 2 keer voor
    ("onderwijzer", 'r'),   # 'r' komt 3 keer voor
    ("telefoneren", 'e')    # 'e' komt 3 keer voor
]


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