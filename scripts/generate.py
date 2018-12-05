""" generate.py

This script creates the time-series data for MLP training.

"""


import sys
import util


def main(args):
    if len(args) < 3:
        print('Usage python3 generate.py <csv-in> <csv-out> <window-size>')
        return

    file_in = args[1]
    file_out = args[2]
    win_size = int(args[3])
    header, data = util.read_csv(file_in)
    new_data = []
    for i in range(len(data) - win_size):
        new_data.append(util.time_series_sample(data, i, win_size))
    util.write_csv(file_out, new_data)


if __name__ == '__main__':
    main(sys.argv)
