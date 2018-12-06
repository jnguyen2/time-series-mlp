""" verify.py

This script verifies that there is no missing data on the interval.

"""
import sys
import util

if len(sys.argv) < 2:
    print('Usage: python3 verify.py <data-file>')
    sys.exit(1)

file_in = sys.argv[1]

header, data = util.read_csv(file_in)

# verify that all timestamps exist
prev_time = int(data[0][0])
interval = 3600
i = 1
while i < len(data):
    if prev_time + interval != int(data[i][0]):
        print('CSV file is missing data.',
              '(Interval = %d)' % (prev_time + interval))
        sys.exit(1)
    prev_time += interval
    i += 1

print('CSV file is good.')
