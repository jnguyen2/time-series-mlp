import sys
import numpy as np
import matplotlib.pyplot as plt

factual = sys.argv[1]
fpredict = sys.argv[2]

actual = np.loadtxt(factual, delimiter=',')
predict = np.loadtxt(fpredict, delimiter=',')

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(actual[:, 0], actual[:, 1], 'g', alpha=0.5)
ax.plot(predict[:, 0], predict[:, 1], 'g')
ax.set_ylim((0, 1))
ax.set_ylabel('Normalized Ozone Concentration')
ax.set_xlabel('POSIX Timestamp (s)')
plt.savefig('/Users/josephnguyen/Desktop/tmp.png', dpi=400)