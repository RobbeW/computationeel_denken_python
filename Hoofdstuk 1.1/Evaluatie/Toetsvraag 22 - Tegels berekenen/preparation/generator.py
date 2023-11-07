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
input block size: 4
output block size: ends with
comparison: exact match
'''

# generate test data
ntests= 20
cases = [(2.1, 3.2, 20.0, "marmeren")]
soorten = ["keramische","natuurstenen","marmeren"]
while len(cases) < ntests:
    h = round(random.uniform(1.5,2.6), 1)
    b = round(random.uniform(1.5, 4.2), 1)
    z = random.randint(3,8) * 5
    soort = random.choice(soorten)
    cases.append( (h, b, z, soort) )

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
        if not(line.startswith( 'Voer' )):
            print(line)
            print(line, file=outfile)

    # add stdout to output file
    # print(stdout, file=outfile, end='')

# add settings to output file
print('-' * 41 + settings, file=outfile, end='')