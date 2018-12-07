""" verify.py

This script verifies that there is no missing data on the interval.

"""
import sys
import numpy as np

if len(sys.argv) < 2:
    print('Usage: python3 verify.py <data-file>')
    sys.exit(1)

file_in = sys.argv[1]

data = np.loadtxt(file_in, delimiter=',')

# verify that all timestamps exist
prev_time = data[0, 0]
interval = 3600
i = 1
while i < len(data):
    if prev_time + interval != int(data[i, 0]):
        print('File is missing data.',
              '(Interval = %d)' % (prev_time + interval))
        sys.exit(1)
    prev_time += interval
    i += 1

print('File is good.')
