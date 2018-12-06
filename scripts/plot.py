import sys
import matplotlib.pyplot as plt
import numpy as np
import util

if len(sys.argv) < 2:
    print('Usage: python3 %s <csv-in> <csv-in>' % sys.argv[0])
    sys.exit(1)

file_in = sys.argv[1]
file_in_two = sys.argv[2]
header, data = util.read_csv(file_in)
data = np.array(data, dtype=float)

header, data_two = util.read_csv(file_in_two)
data_two = np.array(data, dtype=float)

plt.plot(data[:, 0], data[:, 1])
plt.plot(data_two[:, 0], data[:, 1])
plt.show()
