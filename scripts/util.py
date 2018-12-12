""" util.py

Contains common functions used with other scripts.

"""
import datetime
import numpy as np


def parse_date(formatted_string):
    """ Returns a POSIX timestamp of a formatted date-time string.
    Example: 20140526T0600-0600

    Args:
        formatted_string (str): Formatted date-time string.

    Returns:
        int: POSIX timestamp
    """
    year = int(formatted_string[:4])
    month = int(formatted_string[4:6])
    day = int(formatted_string[6:8])
    hour = int(formatted_string[9:11])
    return int(datetime.datetime(year, month, day, hour).timestamp())


def delete_duplicates(data, column):
    """ Removes rows with duplicate values in a matrix. Note that this function
    does not return anything because the deletion is performed in-place.

    Args:
        data (list): Matrix of data.
        column (int): Index of the column containing duplicates.
    """
    keys = set()
    row = 0
    while row < len(data):
        key = data[row][column]
        if key in keys:
            del data[row]
            row -= 1
        keys.add(key)
        row += 1


def filter_data(data, columns):
    """ Removes all columns not in the list of desired columns.

    Args:
        data (list): Matrix of data.
        columns (list): Column indices to keep.

    Returns:
        list: Matrix of data.
    """
    result = []
    for row in data:
        tmp = []
        for index in columns:
            tmp.append(row[index])
        result.append(tmp)
    return result


def time_series_sample(data, idx, win_size):
    """ Generates a rolling window time-series sample.

    Args:
        data (np.array): Matrix containing data.
        idx (int): Starting index.
        win_size (int): Window size.

    Returns:
    """
    if idx >= len(data) - win_size:
        return

    sample = np.ones(win_size + 1, dtype=float)
    for i in range(idx, idx + win_size):
        sample[(i - idx) + 1] = data[i, 1]
    return sample
