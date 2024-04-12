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
python input without prompt: true
block count: multi
input block size: 2
output block size: ends with
comparison: exact match
'''

# generate test data
ntests = 20
cases = [ ("451 254 374 541 671 541", "142 324 841 145 675 324 189 376 450 472 910 705"), ("142 324 841 145 675 324 189 376 450 472 910 705","451 254 374 541 671 541") ]
while len(cases) < ntests:
    card1 = ""
    card2 = ""
    for i in range(6):
        card1 += str(random.randint(1,1500))
        if i != 5:
            card1 += " "
    for i in range(12):
        card2 += str(random.randint(1,1500))
        if i != 11:
            card2 += " "
    
    if random.randint(0,1):
        cases.append( (card1, card2) )
    else:
        cases.append( (card2, card1) )

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
        capture_output=True,
        text=True
    )
  
    result_lines = process.stdout.split("\n")
    for line in result_lines:
        if not(line.startswith( 'Geef' )):
            print(line)
            print(line, file=outfile, end='\n')


    # add stdout to output file
    # print(stdout, file=outfile, end='')

# add settings to output file
print('-' * 41 + settings, file=outfile, end='')