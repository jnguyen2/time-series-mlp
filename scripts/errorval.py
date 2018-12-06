""" checkerrors.py

This script checks the error between two files.

"""
import sys
import numpy as np
import util

if len(sys.argv) < 3:
    print('Usage: python3', sys.argv[0], '<actual-file> <predict-file>')
    sys.exit(1)

actual_file = sys.argv[1]
predict_file = sys.argv[2]

header, actual = util.read_csv(actual_file)
header, predict = util.read_csv(predict_file)

start_idx = 0
while actual[start_idx][0] != predict[0][0]:
    start_idx += 1
actual = actual[start_idx:]

actual = np.array(actual, dtype=float)
actual_y = actual[:, -1]
predict = np.array(predict, dtype=float)
predict_y = predict[:, -1]

mse = np.sum((actual_y - predict_y) ** 2)
print('MSE:', mse)
