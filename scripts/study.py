""" study.py

This script automates the collection of data for the MLP.

"""
import subprocess

# preprocess the data
args = ['python3', 'preprocess.py', '../data/AQDM_raw.csv', '../data/AQDM_pp']
subprocess.run(args)

# normalize the data
args = ['python3', 'normalize.py', '../data/AQDM_pp', '../data/AQDM_hourly']
subprocess.run(args)

# data per day
args = ['python3', 'pick_interval.py', '../data/AQDM_hourly',
        '../data/AQDM_daily', '86400']
subprocess.run(args)

# data per week
args = ['python3', 'pick_interval.py', '../data/AQDM_hourly',
        '../data/AQDM_weekly', '604800']
subprocess.run(args)

# create training data
args = ['python3', 'generate_window.py', '../data/AQDM_hourly',
        '../data/AQDM_hourly_train', '24']
subprocess.run(args)

args = ['python3', 'generate_window.py', '../data/AQDM_daily',
        '../data/AQDM_daily_train', '7']
subprocess.run(args)

args = ['python3', 'generate_window.py', '../data/AQDM_weekly',
        '../data/AQDM_weekly_train', '4']
subprocess.run(args)

print('Training data created.')
print()

hidd_sizes = ['50', '100', '250', '500', '1000', '1500']
for hidd in hidd_sizes:
    print('Testing', hidd, 'hidden nodes.')
    args = ['python3', 'mlp.py', '../data/AQDM_daily_train',
            '../data/AQDM_daily', '../data/daily_mlp_identity_' + hidd, '50',
            hidd, 'identity']
    subprocess.run(args)
    print()

for hidd in hidd_sizes:
    print('Testing', hidd, 'hidden nodes.')
    args = ['python3', 'mlp.py', '../data/AQDM_daily_train',
            '../data/AQDM_daily', '../data/daily_mlp_identity_' + hidd, '50',
            hidd, 'identity']
    subprocess.run(args)
    print()

# mlp performance with different activation functions

# mlp performance with different number of hidden nodes

# regression performance on similar data sets