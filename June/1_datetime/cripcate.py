#!/opt/anaconda/bin/python
"""Python script to display the remaining time until my deadline."""

import datetime as dt
import numpy as np


def get_times(now, then):
    """Calculate the remaining time."""
    total = then - now
    days = total.days
    weeks = total.days // 7
    bus_days = np.busday_count(now, then)
    return weeks, days, bus_days, total


def print_results(weeks, days, bus_days, total):
    """Print the remaining time."""
    print("{} remaining.\n".format(total))
    print("{} weeks and {} days.".format(weeks, days - (weeks * 7)))
    print("{} business days.".format(bus_days))


if __name__ == '__main__':
    deadline = dt.datetime(2017, 12, 1, 23, 59)
    now = dt.datetime.now()

    print_results(*get_times(now, deadline))
