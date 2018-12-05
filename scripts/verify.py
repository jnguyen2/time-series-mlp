""" verify.py

This script verifies that there is no missing data on the interval.

"""

import sys
import util


def main(args):
    if len(args) < 2:
        print('Usage: python3 verify.py <data-file>')
        return

    file_in = args[1]
    header, data = util.read_csv(file_in)
    prev_time = int(data[0][0])
    interval = 3600
    i = 1
    while i < len(data):
        if prev_time + interval != int(data[i][0]):
            print('CSV file is missing data.')
            return
        prev_time += interval
        i += 1
    print('CSV file is good.')


if __name__ == '__main__':
    main(sys.argv)
