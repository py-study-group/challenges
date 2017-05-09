""" The following scripts gets the value of a bitcoin in usd
    and writes that value to a file along with timestamp and then
    graphs a scatter plot of time vs the value of dollar.
"""

import time
import datetime as dt
import urllib.request
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.animation as Animation
from matplotlib import style
import matplotlib
import csv
import threading

style.use('fivethirtyeight')
fig = plt.figure()


def usd_in_bitcoin():  # gets the value of 1 bitcoin in usd
    try:
        resp = urllib.request.urlopen("https://bitcoinwisdom.com/")
    except Exception as e:
        print(e)
    text = resp.read()

    soup = BeautifulSoup(text, 'html.parser')
    intermediate = soup.find('tr', {"id": "o_btcusd"})
    ans = intermediate.find('td', {'class': 'r'})
    return ans.contents[0]


def write_to_file(interval):  # writes the bitcoin value in usd along with timestamp to a file
    while True:
        value = str(usd_in_bitcoin())
        unix_time = str(time.time())
        print(unix_time, value)
        with open('bitcoin_usd.csv', 'a+') as file:
            file.write(unix_time)
            file.write("," + str(value))
            file.write('\n')
        time.sleep(interval)


def animate(i):  # updates the graph continuously
    with open('bitcoin_usd.csv') as csv_file:
        readcsv = csv.reader(csv_file, delimiter=',')
        xs = []
        ys = []
        for row in readcsv:
            if len(row) > 1:
                x, y = [float(s) for s in row]
                xs.append(dt.datetime.fromtimestamp(x))
                ys.append(y)
        print(len(xs))
        dates = matplotlib.dates.date2num(xs)
        fig.clear()
        plt.xlabel("timestamp")
        plt.ylabel("price of a bitcoin in usd")
        plt.plot_date(dates, ys, 'r.-')  # this gives a line instead of scatter plot


def plotting():  # plots the graph
    ani = Animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()


def main():
    a = threading.Thread(name='updating_csv', target=write_to_file, args=(5,))

    a.start()
    time.sleep(5)
    plotting()


''' When we start a program in python it runs in the main thread. Threading module creates child threads.
    Matplotlib used tkinter. Tkinter should always be kept in the main thread.'''

if __name__ == '__main__':
    main()
