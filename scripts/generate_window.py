""" generate.py

This script creates the time-series data for MLP training.

"""
import sys
import numpy as np
import util

if len(sys.argv) < 3:
    print('Usage python3 %s' % sys.argv[0], '<csv-in> <csv-out> <window-size>')
    sys.exit(1)

file_in = sys.argv[1]
file_out = sys.argv[2]
win_size = int(sys.argv[3])

data = np.loadtxt(file_in, delimiter=',')

new_data = []
for i in range(len(data) - win_size):
    new_data.append(util.time_series_sample(data, i, win_size))
new_data = np.array(new_data)

np.savetxt(file_out, new_data, header='generated', delimiter=',', fmt='%.4f')
