""" study.py

This script automates the collection of data for the MLP.

"""
import sys
import subprocess

if len(sys.argv) < 4:
    print('Usage: python3', sys.argv[0], '<train-file> <actual-file>',
          '<summary-file>')
    sys.exit(1)

train_file = sys.argv[1]
actual_file = sys.argv[2]
summary_file = sys.argv[3]

hidd_sizes = ['500', '1000', '1500', '2000']
act_funcs = ['identity', 'logistic', 'tanh', 'relu']
data = []
for func in act_funcs:
    print('Testing %s...' % func)
    for hidd in hidd_sizes:
        print('\tTesting %s...' % hidd)
        args = ['python3', 'mlp.py', train_file, actual_file,
                train_file + '_%s_%s' % (hidd, func), '10', hidd, func]
        proc = subprocess.run(args, stdout=subprocess.PIPE)
        stdout = proc.stdout.decode('UTF-8')
        stdout = stdout.split()
        r2 = float(stdout[3])
        data.append('%s,%s,%.4f' % (func, hidd, r2))

with open(summary_file, 'w') as fh:
    for row in data:
        fh.write(row)
        fh.write('\n')
