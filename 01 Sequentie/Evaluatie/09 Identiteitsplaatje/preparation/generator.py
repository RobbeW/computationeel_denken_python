import os
import importlib.util
import random
import ruamel.yaml
import subprocess

yaml = ruamel.yaml.YAML()



def generate_random_date():
    day = random.randint(1, 31)
    month = random.randint(1, 12)
    year = random.randint(1900, 2100)  # You can adjust the year range as needed
    
    # Ensure valid day for the selected month
    if month in [4, 6, 9, 11]:
        day = min(day, 30)
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            day = min(day, 29)  # Leap year
        else:
            day = min(day, 28)  # Non-leap year
    
    # Format the date as DD/MM/YYYY
    date = f"{day:02d}/{month:02d}/{year}"
    
    return date


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
geloof = ["KAT", "KAT", "KAT", "KAT", "KAT", "KAT", "PRAW", "GR-KAT", "MOJ", "AUG", "ANG", "MAH"]
bloed = ["A", "B", "AB", "O"]
resus = ["+", "-"]
namen = [("Lucas", "Vandenberghe"),
         ("Emma", "Dupont"),
         ("Liam", "Dubois"),
         ("Olivia", "Martens"),
         ("Noah", "Leroy"),
         ("Mila", "Desmet"),
         ("Louis", "Dewitte"),
         ("Alice", "Declercq"),
         ("Leon", "Leclerc"),
         ("Elise", "Van Damme"),
         ("Ethan", "Jacobs"),
         ("Charlotte", "Lambert"),
         ("Victor", "Pauwels"),
         ("Zoe", "De Smet"),
         ("Arthur", "Vanderheyden"),
         ("Sophie", "Lemaire"),
         ("Adam", "Vermeersch"),
         ("Julia", "Dumoulin"),
         ("Hugo", "Vandevelde")]
cases = [ ("Fernand", "Dedecker", 21632, "25/03/1934", "A+", "KAT") ]
for naam in namen:
    cases.append(
        (
          naam[0], naam[1],
          random.randint(10000,99999),
          generate_random_date(),
          random.choice(bloed)+random.choice(resus),
          random.choice(geloof)
        )
    )

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