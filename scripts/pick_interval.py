""" pick_interval.py

This script picks the time data along a different interval.

"""
import sys
import numpy as np

if len(sys.argv) < 3:
    print('Usage: python3', sys.argv[0], '<input-file> <output-file>',
          '<interval>')
    sys.exit(1)

infile = sys.argv[1]
outfile = sys.argv[2]
interval = int(sys.argv[3])

indata = np.loadtxt(infile, delimiter=',')

newdata = []
for i in range(0, np.shape(indata)[0], interval // 3600):
    newdata.append(indata[i])
newdata = np.array(newdata)

np.savetxt(outfile, newdata, header='interval=%d' % interval, delimiter=',',
           fmt='%.4f')
