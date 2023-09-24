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
input block size: 4
output block size: ends with
comparison: exact match
'''

# generate test data
ntests= 20
names = [("Wout","Aernout"),
         ("Jawdat", "Al-Nakeeb"),
         ("Anton", "Rares-Andrei"),
         ("Laura", "Bisschop"),
         ("Julie", "Bosschem"),
         ("Jacquine", "Cambré"),
         ("Mathis","De Buck"),
         ("Arno","De Vos"),
         ("Margot", "De Wasch"),
         ("Lucas","Eeckhaut"),
         ("Hanne","Geldof"),
         ("Hannes","Leliaert"),
         ("Louka","Meesens"),
         ("Ferre","Peers"),
         ("Maxime","Penninck"),
         ("Bertine","Rollier"),
         ("Loran","Rottiers")]
cases = [("Mathieu", "De Baets", "Rufus", "Morael")]
while len(cases) < ntests:
    pers1 = random.choice(names)
    pers2 = random.choice(names)
    if pers1 != pers2:
        cases.append( (pers1[0], pers1[1], pers2[0], pers2[1]) )
    
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
