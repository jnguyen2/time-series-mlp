import sys
import numpy as np
import matplotlib.pyplot as plt

fin = sys.argv[1]

data = []
with open(fin, 'r') as fh:
    for row in fh:
        data.append(row.strip().split(','))

for i in range(len(data)):
    data[i] = data[i][1:]
data = np.array(data, dtype=float)

xs = data[:4, 0]
id_ys = data[:4, 1]
log_ys = data[4:8, 1]
tan_ys = data[8:12, 1]
relu_ys = data[12:16, 1]

fig, ax = plt.subplots()
ax.plot(xs, id_ys, 'ro--')
ax.plot(xs, log_ys, 'yo--')
ax.plot(xs, tan_ys, 'go--')
ax.plot(xs, relu_ys, 'bo--')

for i, j in zip(xs, id_ys):
    ax.annotate(str(j), xy=(i, j))
for i, j in zip(xs, log_ys):
    ax.annotate(str(j), xy=(i, j))
for i, j in zip(xs, tan_ys):
    ax.annotate(str(j), xy=(i, j))
for i, j in zip(xs, relu_ys):
    ax.annotate(str(j), xy=(i, j))

ax.set_xticks([500, 1000, 1500, 2000])

plt.show()
