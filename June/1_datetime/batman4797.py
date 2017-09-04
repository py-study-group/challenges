#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QLCDNumber
from PyQt5.QtCore import QTimer, QTime
from datetime import datetime, timedelta
import time, os,sys
import timegui

start_time = datetime.now()


class whatsleft():

    def getinfo(self):

        os.system("clear||cls")
        print("\nI have selected B4TM4N-D4Y for calculating this challenge\n")

        # Batman-Day's Datetime info
        Batman_Day = '9/26/2017'
        print("B4TM4N-D4Y is {}\n".format(Batman_Day))
        parse = "%m/%d/%Y"
        self.Batman_Day_dt = datetime.strptime(Batman_Day,parse)

        # Today's Datetime info
        self.today_dt = datetime.now()

    def thismuchleft(self):

        # calculating remaining Datetime info
        remaining_dt = self.Batman_Day_dt - self.today_dt
        time_remained = str(remaining_dt)
        self.rem_days = int(time_remained.split()[0])
        self.rem_weeks = self.rem_days//7
        self.ltovr_days  = self.rem_days%7
        ltovr_time = time_remained.split()[2]

        print("Remaining weekdays calculation changes with selected Day\nMy selected day B4TM4N-D4Y is on Tuesday .. \
              \nso calculating remaining weekdays based on this...\n")

        if self.ltovr_days > 2:
            ltovr_weekdays = self.ltovr_days -2
        elif self.ltovr_days == 0:
            ltovr_weekdays = 0
        elif self.ltovr_days in [1,2]:
            ltovr_weekdays = 1

        self.rem_weekdays = (self.rem_weeks * 5 )+ ltovr_weekdays
        self.rem_abs_time = "{}:{}".format(self.rem_days,ltovr_time)
        self.elapsed = str(datetime.now() - start_time)

    def main(self):
        try:
            while True:
                self.getinfo()
                self.thismuchleft()
                print("\n\t{} weeks with {} left over day(s) and\n".format(self.rem_weeks,self.ltovr_days))
                print("\t{} days out of them {} working days\n".format(self.rem_days,self.rem_weekdays))
                print("\tare REMAINING TILL B4TM4N-D4Y\n".format())
                print("\tAbsolute Time remained is {}  ".format(self.rem_abs_time))
                print("\n\tTime passed after program has been started is {} seconds".format(self.elapsed))
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nThanks for running the script\n")
            raise SystemExit

if __name__ == "__main__":
    myday = whatsleft()
    myday.main()
