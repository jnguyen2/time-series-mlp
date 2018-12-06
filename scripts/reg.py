""" reg.py

This script trains a linear regressor.

"""
import sys
import warnings
import numpy as np
from sklearn.linear_model import LinearRegression
import util

warnings.filterwarnings('ignore')
if len(sys.argv) < 2:
    print('Usage: python3', sys.argv[0], '<train-file> <iterations>')
    sys.exit(1)

file_in = sys.argv[1]
iterations = int(sys.argv[2])

# read in data
header, data = util.read_csv(file_in)
data = np.array(data, dtype=float)
win_size = np.shape(data)[1]
test_idx = np.shape(data)[0] - 2 * (np.shape(data)[0] // 10)

total_rmse = 0.0
total_accuracy = 0.0
for _ in range(iterations):
    np.random.shuffle(data)
    train_data = data[:test_idx, :]
    test_data = data[test_idx:, :]

    train_inputs = train_data[:, :-1]
    train_targets = train_data[:, -1]

    test_inputs = test_data[:, :-1]
    test_targets = test_data[:, -1]

    reg = LinearRegression().fit(train_inputs, train_targets)
    predictions = reg.predict(test_inputs)

    rmse = np.sqrt(np.sum((predictions - test_targets) ** 2) /
                   np.shape(predictions)[0])
    accuracy = reg.score(test_inputs, test_targets)
    total_rmse += rmse
    total_accuracy += accuracy

print('RMSE:', total_rmse / iterations)
print('Mean Accuracy:', total_accuracy / iterations)
