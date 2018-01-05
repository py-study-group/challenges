#! python3

"""
Class to find the weeks, days and hours count from the current system date 
to a target date.  To change the target date, update the input values
of the DateDiff instantiation.
"""

import datetime as dt

class DateDiff(object):
    
    def __init__(self, month = 12, day = 31, year = 2017):
        """ 
        month: int. Target month.
        day: int. Target day.
        year: int.  Target year.
        end: datetime.  Target end date and time datetime object.
        currentDT: datetime.  Initialize datetime.
        """
        self.month = month
        self.day = day
        self.year = year
        self.end = dt.datetime(self.year, self.month, self.day, 0, 0, 0)
        self.currentDT = dt.datetime.now()

    def weeksLeft(self, delta):
        """
        Returns the weeks and days left until the target date.  

        delta: timedelta
        return: string
        """
        targetWeek = dt.date(self.year, self.month, self.day).isocalendar()[1]
        currentWeek = (dt.date(self.currentDT.year, self.currentDT.month, self.currentDT.day).isocalendar()[1]) 

        weekCount = targetWeek - currentWeek 
        # If no more weeks left, count days until target.  Otherwise, count days left in week.
        if weekCount == 0:
            daysLeft = delta
        else:
            weekCount -= 1
            dayOfWeek = self.currentDT.weekday()  
            daysLeft = dt.timedelta(days=6 - self.currentDT.weekday())

        return "{0} weeks, {1} days left".format(str(weekCount), daysLeft.days)

    def daysLeft(self, delta):
        """ 
        Returns a string with the timedelta.days value, which is a count of 
        the days left until the target date.

        delta: timedelta
        return: string.
        """
        return "{0} days left".format(delta.days)

    def busDaysLeft(self):
        """
        Count the weekdays left until the target date.  Uses the toordinal 
        and fromordinal functions to get a range of values for the current
        date and the target date, then loops through the range to count the
        weekdays left.

        return: string.
        """
        weekdayCount = -1 # neg count to burn today's date.
        startOrd = self.currentDT.toordinal()
        endOrd = self.end.toordinal()
        
        for i in range(startOrd, endOrd):
            checkDay = dt.datetime.fromordinal(i)

            if checkDay.weekday() not in[5,6]:
                weekdayCount += 1

        return "{0} business days left".format(weekdayCount)

    def datetimeLeft(self, delta):
        """ 
        Use the delta duration value to calculate the remaining days, hours, 
        minutes and seconds left until the target date.  Returns a string with 
        the duration for days, hours minutes and seconds.

        delta: timedelta
        return: string.
        """
        days, seconds = delta.days, delta.seconds
        hours = (seconds // 3600)
        minutes = (seconds % 3600) // 60
        seconds = (seconds % 60)

        return "{0} days {1} hours {2} minutes {3} seconds".format(days, hours, minutes, seconds)
    
    def diffCalc(self):
        """
        Sets the current date and time used for the class, and calculates 
        the timedelta input value for the class functions. Prints results 
        from days/time left class functions.
        """
        self.currentDT = dt.datetime.now()
        deltaDays = self.end - self.currentDT      
  
        print(self.__str__())
        print(self.weeksLeft(deltaDays))
        print(self.daysLeft(deltaDays))
        print(self.busDaysLeft())
        print(self.datetimeLeft(deltaDays))

        return ""

    def __str__(self):
        """
        Returns the target date set for the class.
        """
        return "Target date is {0}/{1}/{2}".format(self.month, self.day, self.year)

if __name__ == "__main__":
    dateDiff = DateDiff(12, 31, 2017)
    print(dateDiff.diffCalc())
