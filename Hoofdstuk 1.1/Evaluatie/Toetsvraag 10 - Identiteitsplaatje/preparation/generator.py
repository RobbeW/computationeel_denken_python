import os
import random
import subprocess
from typing import Text

# set fixed seed for generating test cases
random.seed(123456789)

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join('..', 'solution')
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

# configuration settings
tab_name = 'Feedback'
settings = f'''
tab name: {tab_name}
python input without prompt: false
block count: multi
input block size: 6
output block size: ends with
comparison: exact match
'''

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


# configure test files
infile = open(os.path.join(evaldir, '0.in'), 'w')
outfile = open(os.path.join(evaldir, '0.out'), 'w')

# generate unit tests
for stdin in cases:

    # add input to input file
    stdin = '\n'.join(f'{line}' for line in stdin)
    print(stdin, file=infile)

    # generate output to output file
    script = os.path.join(solutiondir, 'solution.nl.py')
    process= subprocess.run(
        ['python3', script],
        input=stdin,
        encoding='utf-8',
        capture_output=True
    )
        
    result_lines = process.stdout.split("\n")
    for line in result_lines:
        if not(line.startswith( 'Geef' )):
            print(line)
            print(line, file=outfile)

    # add stdout to output file
    # print(process.stdout, file=outfile, end='')

# add settings to output file
print('-' * 41 + settings, file=outfile, end='')
