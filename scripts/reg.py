""" reg.py

This script trains a linear regressor.

"""
import sys
import warnings
import numpy as np
from sklearn.linear_model import LinearRegression
import util

warnings.filterwarnings('ignore')

if len(sys.argv) < 5:
    print('Usage: python3', sys.argv[0], '<train-file> <actual-file>',
          '<output-file> <iterations>')
    sys.exit(1)

train_file = sys.argv[1]
actual_file = sys.argv[2]
output_file = sys.argv[3]
iterations = int(sys.argv[4])

# read in data
data = np.loadtxt(train_file, delimiter=',')
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
print('R^2:', total_accuracy / iterations)

data = np.loadtxt(actual_file, delimiter=',')
new_data = []
for i in range(len(data) - win_size):
    timestamp = data[i + win_size][0]
    sample = util.time_series_sample(data, i, win_size)
    sample = np.reshape(np.array(sample, dtype=float), (1, -1))
    row = [timestamp, reg.predict(sample[:, :-1])[0]]
    new_data.append(row)
new_data = np.array(new_data)
np.savetxt(output_file, new_data, header='regression', delimiter=',',
           fmt='%.4f')
