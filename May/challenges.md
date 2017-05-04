# Monthly programming challenges for the study.py group

Hello dear members, it's time to announce our first monthly coding challenges.

To cover the wide range of different skill levels and different programming interests among the group, I have created challenges in multiple categories. For the first month (May) these are:

1. Beginner
2. Web-Scraping
3. Data

As this is my first attempt at creating challenges for everyone, please give me as much feedback as you can, so I can improve for next month. tell me whether specific aspects were unclear, tasks were too easy / hard, projects were too large etc. etc. Based on interest and response to the challenges I will vary them for next month!

Also let me know if you want some sort of "grading system". Or something like a "coder of the month" award for the challenges. The first monthly challenge will be a **beta** and therefore no grading will be done. The solutions to the problems can be uploaded until the end of the month. I will think about an appropriate way of sharing solutions until then (github / slack).

Here we go:

## [Beginner] Morse Code

Morsing is a technique that fewer and fewer people know how to use. Good thing you are a programmer and able to develop a program to translate normal text into morse code and vice versa! This will give you practise in transforming strings and working with dictionaries.

**Problem:**

Write a program that takes a string as an input and translates it into morse code. Example: `"Hello, World" == ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.."`. You can try morse-code translation on [this website](https://morsecode.scphillips.com/translator.html)

**Bonus:**

Read in a textfile of written english language. Transform it to morse code with your program and save the result in a new textfile. This will teach you how to open and save files with python. Also try to catch special characters (.,:;" etc.) so that your program doesn't break when they occur.

## [Web-Scraping] Cryptocurrencies

Bitcoins and other cryptocurrencies are on the rise. The Brexit and election of president Trump contributed to the immense increase of the BTC:EUR over the last year. Monitoring exchange rates and predicting the behaviour of the bitcoin price can be crucial in trading.

**Problem:**

Navigate to this [homepage](https://bitcoinwisdom.com/) with listings of bitcoin exchange rates. Choose the exchange rate for a currency of your choice (USD, EUR, etc.) and save it (to textfile, csv, sql database, your choice). Query this information in regular time intervals (10 seconds, 5 minutes, once a day, your choice) and update your stored data accordingly. Attach a timestamp to every exchange rate you scraped.

If you need a machine running 24/7 to perform the scraping contact me or anyone in the group with AWS to host your script.

**Bonus:**

Visualize your gathered data in an appropriate way.

## [Data] Crime Rates

**Problem:**

[This website](https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/1tabledatadecoverviewpdf/table_1_crime_in_the_united_states_by_volume_and_rate_per_100000_inhabitants_1994-2013.xls) displays a dataset of crime rates in the US over a 20 year period.

Eplore the dataset using pythons native data analysis libraries (numpy, pandas, matplotlib, sklearn, etc.). Visualize the time-data highlighting the most interesting aspects. Try to answer the following questions:

* Are there unusual developments in crime rate? (unusually high/low in different categories)
* Is there a specific trend at which murder / theft rates increase or decrease? (try to apply regression methods)
* Do certain types of crime correlate? (eg. high burglary rate = also high property crime rate)

Try to quantify your findings like "usually there are 0.7 times as much murders as aggravated assaults"

**Bonus:**

1. Wrap your analysis up in a report in form of a jupyter notebook, or a markdown document that shows and explains your python code and highlights important diagrams.
2. Try to predict crime rates for the year 2014. Then try to find actual data for 2014 and compare your results.

----

I hope the challenges are interesting, and of the right difficulty levels. Noone should feel to nooby or to elite to solve them. It is encouraged that you work in groups and communicate to overcome obstacles. Wolutions to the problems can also be published in teams.

Happy coding.
