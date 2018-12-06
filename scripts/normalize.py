""" normalize.py

This script normalizes the data values in the time-series.

"""
import sys
from sklearn.preprocessing import MinMaxScaler
import numpy as np

if len(sys.argv) < 3:
    print('Usage: python3', sys.argv[0], '<input-file> <output-file>')
    sys.exit(1)

file_in = sys.argv[1]
file_out = sys.argv[2]

data = np.loadtxt(file_in, dtype=float, delimiter=',')

# normalize second column
values = np.reshape(data[:, 1], (-1, 1))
minmax_scaler = MinMaxScaler()
data[:, -1] = np.reshape(minmax_scaler.fit_transform(values), (1, -1))

np.savetxt(file_out, data, header='normalized', fmt='%.4f', delimiter=',')
