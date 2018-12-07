""" unnormalize.py

This script unnormalizes the data.

"""
import sys
import numpy as np
from sklearn.preprocessing import MinMaxScaler

if len(sys.argv) < 3:
    print('Usage: python3', sys.argv[0], '<input-file> <original-file>',
          '<output-file>')
    sys.exit(1)

in_file = sys.argv[1]
orig_file = sys.argv[2]
out_file = sys.argv[3]

in_data = np.loadtxt(in_file, dtype=float, delimiter=',')
orig_data = np.loadtxt(orig_file, dtype=float, delimiter=',')

scaler = MinMaxScaler()
in_vals = np.reshape(in_data[:, 1], (-1, 1))
fit_vals = np.reshape(orig_data[:, 1], (-1, 1))
scaler.fit(fit_vals)
in_vals = scaler.inverse_transform(in_vals)
in_data[:, 1] = np.reshape(in_vals, (1, -1))

np.savetxt(out_file, in_data, header='unnormalized', fmt='%.4f', delimiter=',')
