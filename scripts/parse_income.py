import sys
import time

from util import parse_csv


def main(args):
    if len(args) < 2:
        return

    fname = args[1]
    zipcode = args[2]

    tic = time.time()
    data = parse_csv(fname)
    toc = time.time()
    print('CSV parsed in %.2fs.' % (toc - tic))

    header = data[0]
    zip_idx = header.index('zipcode')
    n1_idx = header.index('N1')
    agi_idx = header.index('A00100')

    total_filed = 0
    total_agi = 0
    for row in data:
        if row[zip_idx] == zipcode:
            total_filed += int(row[n1_idx])
            total_agi += int(row[agi_idx])
    print('Zipcode:', zipcode)

    if total_filed == 0:
        print('No data.')
    else:
        print('AGI per file:', total_agi / total_filed)


if __name__ == '__main__':
    main(sys.argv)
