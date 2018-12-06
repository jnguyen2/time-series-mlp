""" preprocess.py

This script cleans up the original AQDM data file.

"""
import sys
import csv
import numpy as np
import util

if len(sys.argv) < 3:
    print('Usage: python3 %s' % sys.argv[0], '<input-file> <output-file>')
    sys.exit(1)

# command-line arguments
file_in = sys.argv[1]
file_out = sys.argv[2]

# read in data
data = []
with open(file_in, 'r') as handle:
    reader = csv.reader(handle)
    for row in reader:
        data.append(row)
header = data[0]
data = data[1:]

# convert formatted timestamps to posix timestamps
header.append('posix')
date_idx = header.index('datetime')
for i in range(len(data)):
    date = data[i][date_idx]
    posix = util.parse_date(date)
    data[i].append(posix)

# sort and delete duplicates
data = sorted(data, key=lambda sample: sample[-1])
util.delete_duplicates(data, -1)

# remove unused columns
posix_idx = header.index('posix')
ppm_idx = header.index('value')
columns = [posix_idx, ppm_idx]
data = util.filter_data(data, columns)

# fill in new data
new_data = []
new_data.append(data[0])
prev_time = data[0][0]
prev_val = data[0][1]
interval = 3600
i = 1
while i < len(data):
    new_time = prev_time + interval
    if new_time == data[i][0]:
        new_data.append(data[i])
        prev_time = data[i][0]
        prev_val = data[i][1]
        i += 1
    else:  # handling missing values
        new_data.append([new_time, prev_val])
        prev_time = new_time

# write data with header
new_data = np.array(new_data, dtype=float)
np.savetxt(file_out, new_data, header='preprocessed',
           delimiter=',', fmt='%.4f')
