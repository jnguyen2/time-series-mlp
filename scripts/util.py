import sys


def parse_csv(fname):
    data = []
    with open(fname, 'r') as fh:
        for line in fh:
            line = line.strip()
            row = line.split(',')
            data.append(row)
    return data


def main(args):
    if len(args) < 2:
        return

    fname = args[1]

    data = parse_csv(fname)
    print(data[0])
    print(len(data))


if __name__ == '__main__':
    main(sys.argv)
