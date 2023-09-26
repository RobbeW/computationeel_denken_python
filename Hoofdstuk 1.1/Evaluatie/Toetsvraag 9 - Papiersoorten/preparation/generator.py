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
cases = [ ("A", 4, 297, 210),
          ("A", 3, 420, 297),
          ("A", 2, 594, 420),
          ("A", 1, 841, 594),
          ("A", 0, 1189, 841),
          ("B", 0, 1414, 1000),
          ("B", 1, 1000, 707),
          ("B", 2, 1000, 500),
          ("B", 3, 500, 353),
          ("C", 0, 1297, 917),
          ("C", 1, 917, 648),
          ("C", 2, 648, 458),
          ("C", 3, 458, 324)]


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
