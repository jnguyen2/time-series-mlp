import sys
import matplotlib.pyplot as plt
import numpy as np
import util


def main(args):
    if len(args) < 2:
        print('Usage: python3 plot.py <csv-in>')
        return

    file_in = args[1]
    header, data = util.read_csv(file_in)
    data = np.array(data, dtype=float)
    plt.plot(data[:, 0], data[:, 1])
    plt.show()


if __name__ == '__main__':
    main(sys.argv)
