""" generate.py

This script creates the time-series data for MLP training.

"""


import sys
import numpy as np
import util


def sample(data, index, interval):
    """ Creates a sample for the time-series data set from the given index.

    Args:
        data (list): Matrix of data.
        index (int): Start index.
        interval (int): Time interval.

    Returns:
        list: Interval sample.
    """
    result = []
    result.append(data[index][1])
    prev_val = data[index][0]
    index += 1
    while index < len(data) and len(result) < 6:
        curr_val = prev_val + interval
        if data[index][0] == curr_val:
            result.append(data[index][1])
        else:
            return []
        prev_val = curr_val
        index += 1
    return result


def main(args):
    if len(args) < 3:
        print('Usage python3 generate.py <csv-in> <csv-out>')
        return

    file_in = args[1]
    file_out = args[2]

    data = util.read_csv(file_in)
    data = data[1:]

    for i in range(len(data)):
        data[i][0] = int(data[i][0])
        data[i][1] = float(data[i][1])

    new_data = []
    for i in range(len(data)):
        tmp = sample(data, i, 3600)
        if len(tmp) == 6:
            new_data.append(tmp)
    util.write_csv(file_out, new_data)


if __name__ == '__main__':
    main(sys.argv)
