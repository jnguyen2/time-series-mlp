""" mlp.py

This script trains an MLP using the sampled data.

"""
import sys
import util
import numpy as np
from sklearn.neural_network import MLPRegressor

if len(sys.argv) < 3:
    print('Usage: python3 %s' % sys.argv[0], '<training-file> <actual-file>',
          '<output-file> <iterations> <hidden-one> <hidden-two>',
          '<early-stopping>')
    sys.exit(1)

train_file = sys.argv[1]
actual_file = sys.argv[2]
output_file = sys.argv[3]
iterations = int(sys.argv[4])
nhiddone = int(sys.argv[5])
nhiddtwo = int(sys.argv[6])
early_stop = True if sys.argv[7] == '1' else False

data = np.loadtxt(train_file, delimiter=',')

# train mlp for specified number of iterations
total_rmse = 0.0
total_accuracy = 0.0
for _ in range(iterations):
    np.random.shuffle(data)
    win_size = np.shape(data)[1]
    test_idx = np.shape(data)[0] - 2 * (np.shape(data)[0] // 10)

    train_data = data[:test_idx, :]
    test_data = data[test_idx:, :]

    train_inputs = train_data[:, :-1]
    train_targets = train_data[:, -1]

    test_inputs = test_data[:, :-1]
    test_targets = test_data[:, -1]

    mlp = MLPRegressor(hidden_layer_sizes=(nhiddone, nhiddtwo),
                       activation='logistic', early_stopping=early_stop,
                       max_iter=1000)
    mlp = mlp.fit(train_inputs, train_targets)

    predictions = mlp.predict(test_inputs)
    rmse = np.sqrt(np.sum((predictions - test_targets) ** 2) /
                   np.shape(predictions)[0])
    accuracy = mlp.score(test_inputs, test_targets)

    total_rmse += rmse
    total_accuracy += accuracy

print('RMSE:', total_rmse / iterations)
print('R^2:', total_accuracy / iterations)

# predict on actual file
data = np.loadtxt(actual_file, delimiter=',')
new_data = []
for i in range(len(data) - win_size):
    timestamp = data[i + win_size][0]
    sample = util.time_series_sample(data, i, win_size)
    sample = np.reshape(np.array(sample, dtype=float), (1, -1))
    row = [timestamp, mlp.predict(sample[:, :-1])[0]]
    new_data.append(row)
new_data = np.array(new_data)

np.savetxt(output_file, new_data, header='mlp predicted', delimiter=',',
           fmt='%.4f')
