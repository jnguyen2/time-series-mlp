""" preprocess.py

This script cleans up the original AQDM data file.

"""

import sys
import util


def main(args):
    """ Main function. """
    if len(args) < 3:
        print('Usage: python3 %s <csv-in> <csv-out>' % sys.argv[0])
        return

    # command-line arguments
    file_in = sys.argv[1]
    file_out = sys.argv[2]
    data = util.read_csv(file_in)

    # convert formatted timestamps to posix timestamps
    header = data[0]
    header.append('posix')
    data = data[1:]
    date_idx = header.index('datetime')
    for i in range(len(data)):
        date = data[i][date_idx]
        posix = util.parse_date(date)
        data[i].append(posix)

    # sort and delete duplicates
    data = sorted(data, key=lambda sample: sample[-1])
    util.delete_duplicates(data, -1)

    # remove unused columns
    posix_index = header.index('posix')
    ppm_index = header.index('value')
    columns = [posix_index, ppm_index]
    data = util.filter_data(data, columns)

    new_data = []
    new_data.append(data[0])
    prev_val = data[0][0]
    interval = 3600
    for i in range(1, len(data)):
        if (prev_val + interval - data[i][0]) % interval == 0:
            new_data.append(data[i])
            prev_val = data[i][0]

    # write csv to file with header
    header = ['time', 'ppm']
    new_data.insert(0, header)
    util.write_csv(file_out, new_data)


if __name__ == '__main__':
    main(sys.argv)
