import sys
import numpy as np
import matplotlib.pyplot as plt

fin = sys.argv[1]

data = np.loadtxt(fin, delimiter=',')

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(data[:, 0], data[:, 1], 'g')
ax.axhline(0.1, color='r', linestyle='--')
ax.axhline(0.07, color='y', linestyle='--')
ax.set_ylabel('Ozone Concentration (ppm)')
ax.set_xlabel('POSIX Timestamp (s)')
plt.savefig('/Users/josephnguyen/Desktop/tmp.png', dpi=400)
