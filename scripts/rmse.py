""" checkerrors.py

This script checks the error between two files.

"""
import sys
import numpy as np

if len(sys.argv) < 3:
    print('Usage: python3', sys.argv[0], '<actual-file> <predict-file>')
    sys.exit(1)

actual_file = sys.argv[1]
predict_file = sys.argv[2]

actual = np.loadtxt(actual_file, delimiter=',')
predict = np.loadtxt(predict_file, delimiter=',')

start_idx = 0
while start_idx < np.shape(actual)[0] and \
      actual[start_idx, 0] != predict[0, 0]:
    start_idx += 1
if start_idx == len(actual):
    print('Reached end somehow.')
    sys.exit(1)
actual = actual[start_idx:, :]

actual_y = actual[:, -1]
predict_y = predict[:, -1]

rmse = np.sqrt(np.sum((actual_y - predict_y) ** 2) / np.shape(actual)[0])
print('RMSE:', rmse)
