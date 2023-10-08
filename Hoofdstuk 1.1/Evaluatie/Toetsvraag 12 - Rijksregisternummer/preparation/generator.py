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
input block size: 5
output block size: ends with
comparison: exact match
'''


# generate test data
ntests = 20
cases = [ ("85", "02", "01", "002", "00") ]
while len(cases) < ntests:
    gebjaar = random.randint(1980, 2012) % 100
    gebmaand = random.randint(1,12)
    gebdag = random.randint(1,31)
    dagteller = random.randint(2,400)
    getal = dagteller + gebdag * 10**3 + gebmaand * 10**5 + gebjaar * 10**7
    if gebjaar < 13:
        getal += 2 * 10**9
    controlegetal = 97 - getal % 97
    cases.append( (str(gebjaar).zfill(2), str(gebmaand).zfill(2), str(gebdag).zfill(2), str(dagteller).zfill(3), str(controlegetal).zfill(2)))


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
