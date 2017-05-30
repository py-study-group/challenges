"""
The subquestions have been answered in various functions. To get the answer of a question, simply type the function in
last line

The various available functions are:
1) plotting() : This function plots all the data of the crime rates

2) unusual_developments_in_crime()  : This function finds the type of crime which has the highest difference in
   its maximum and min value over the years

3) regression_murder(year): This function applies linear regression on crimes of the type "murder" and can be used
   to predict the expected murder rates in the "year" parameter of the function, which you give as an input.
   It also shows a plot of the linear regression line and prints the expected murder rate in the year mentioned on
   the screen.

"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

style.use('bmh')


def get_data_frames():
    l = [0, 1, 2]
    for i in range(24, 38):
        l.append(i)
    df = pd.read_excel('crime_table.xls', skiprows=l).iloc[:20]

    df.set_value(7, 'Year', 2001)
    df.set_value(18, 'Year', 2012)
    df.set_index('Year', inplace=True)
    df.drop(df.columns[[19, 20, 21, 22]], axis=1,
            inplace=True)  # axis=1 means we are referring to a col not a row
    x = []
    df.rename(columns={'Population1': 'Population'}, inplace=True)
    crime_rate_df = df.copy(deep=True)
    population_df = df['Population']
    for i in range(1, 10):
        x.append(2 * i)
    crime_rate_df.drop(crime_rate_df.columns[x], axis=1, inplace=True)
    crime_rate_df.drop(crime_rate_df.columns[[0]], axis=1, inplace=True)
    indexes = list(crime_rate_df.index.values)
    for i in range(len(indexes)):
        crime_rate_df.iloc[i] = (crime_rate_df.iloc[i] / population_df.iloc[i]) * 100000  # the crime rate is wrt
        # 100,000 as base population

    total_crime_df = crime_rate_df.mean(axis=1)  # axis =1 means row wise and axis = 0 means col wise

    perc_change = crime_rate_df.copy(deep=True)
    perc_change = (perc_change / perc_change.iloc[0] - 1) * 100
    total_crime_perc_change = perc_change.mean(axis=1)

    return df, crime_rate_df, population_df, perc_change, total_crime_perc_change, total_crime_df


def plotting():  # plots the various crime rates
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    perc_change.plot(ax=ax1, linewidth=3)
    total_crime_perc_change.plot(ax=ax1, linewidth=10, color='black', label='mean crime rate')

    ax1.legend(loc="lower left")
    plt.title("Percentage change in crime rates compared to starting year")
    plt.show()


def unusual_developments_in_crime():
    max_min = pd.DataFrame()
    max_min['max'] = crime_rate_df.max(axis=0)
    max_min['min'] = crime_rate_df.min(axis=0)
    max_min['abs'] = max_min['max'] - max_min['min']

    max_abs = max_min['abs'].max(axis=0)

    crime_type_max_change = max_min[max_min['abs'] == max_abs].index.tolist()
    print("%s has the highest change in max and min value of the crime with difference being %s" % (
        crime_type_max_change[0], max_abs))


def regression_murder(year):  # applies linear regression on murder rates
    murder = pd.DataFrame()
    dates = crime_rate_df.index.values.tolist()
    murder['label'] = crime_rate_df['Murder and\nnonnegligent \nmanslaughter']
    prediction_size = int(0.1 * len(murder))

    X = np.array(dates)
    y = np.array(murder['label'])
    y.reshape((len(X), 1))
    y_train = y[:-prediction_size]
    X_train = X[:-prediction_size]
    clf = LinearRegression()

    clf.fit(X_train.reshape(-1, 1), y_train)
    regression_line = [clf.predict(X_train[i].reshape(1, -1)) for i in range(len(X_train))]
    print(clf.predict(year))
    plt.scatter(X_train, y_train)
    plt.plot(X_train, regression_line)
    plt.show()


df, crime_rate_df, population_df, perc_change, total_crime_perc_change, total_crime_df = get_data_frames()
