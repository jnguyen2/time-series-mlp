""" mlp.py

This script trains an MLP using the sampled data.

"""


import sys
import util
import numpy as np
from sklearn.neural_network import MLPRegressor


def main(args):
    if len(args) < 3:
        print('Usage: python3 mlp.py <training-file> <actual-file>',
              '<hidden-one> <hidden-two> <early-stopping>')
        return

    train_file = args[1]
    actual_file = args[2]
    nhiddone = int(args[3])
    nhiddtwo = int(args[4])
    early_stop = True if args[5] == '1' else False

    data = np.loadtxt(train_file, dtype=float, delimiter=',')
    np.random.shuffle(data)
    win_size = np.shape(data)[1]
    test_idx = np.shape(data)[0] - (np.shape(data)[0] // 10)

    train_data = data[:test_idx, :]
    test_data = data[test_idx:, :]
    np.random.shuffle(train_data)

    train_inputs = train_data[:, :-1]
    train_targets = train_data[:, -1]

    test_inputs = test_data[:, :-1]
    test_targets = test_data[:, -1]

    mlp = MLPRegressor(hidden_layer_sizes=(nhiddone, nhiddtwo),
                       activation='identity', early_stopping=early_stop)
    mlp.fit(train_inputs, train_targets)

    predictions = mlp.predict(test_inputs)
    rmse = np.sqrt(np.sum((predictions - test_targets) ** 2) /
                   np.shape(predictions)[0])

    print('RMSE:', rmse)
    print('Mean Accuracy:', mlp.score(test_inputs, test_targets))
    print(mlp.n_layers_)

    header, data = util.read_csv(actual_file)
    for i in range(len(data) - win_size):
        timestamp = data[i + win_size][0]
        sample = util.time_series_sample(data, i, win_size - 1)
        sample = np.reshape(np.array(sample, dtype=float), (1, -1))
        print(timestamp, mlp.predict(sample)[0])


if __name__ == '__main__':
    main(sys.argv)
