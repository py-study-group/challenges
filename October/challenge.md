# Monthly programming challenge for the study.py group

## Write a small Command Line program that is able to process only CSV files and provides the following options.

1. --file Specify a file to process.
2. --http-get-file Download and process a file from the web
3. --output-file Define an output file.
4. --merge-files Merge all given files into a single-one.
5. --get-line Return a file line, based on the given line-number.
6. --remove-line Delete a file line, based on the given line-number.
7. --filter Return all lines containing the given filter words.

### Input File Arguments

Input file arguments are `--file`, `--http-get-file` and `--merge-files` and are mutually exclusive meaning that your script will only allow one of these three arguments. The input file argument is what gets acted upon by the action arguments.

The only exception is the `--merge-files` which is both a data argument and a specific action (merge the files provided) before taking action.

#### file argument

Reads the csv file provided as a parameter to the argument and passes that to the action.

#### http-get-file argument

Downloads and reads the file provided as a parameter to the argument and passes that to the action.

#### merge-files argument

Combines the parameters provided into one and passes that to the action arguments.

### Action Arguments

The action arguments are `--get-line`, `--remove-line` and `--filter`. They take the data provided by the Data Arguments and perform some action on them.

#### get-line

Prints the corresponding data to the screen of that row in the csv.

#### remove-line

Removes the corresponding row of data. If `--output-file` is provided it saves the resulting file else it prints it to the screen.

#### filter

Finds each row that contain a word in the provided arguments and if `--output-file` is provided it saves the results to the file, else it prints the results to the screen.


### Output File Arguments

Saves the results of the action taken on the Input(s) to the provided file.

### Examples

    python csv_script.py --file "/home/tjcim/Projects/csv_files/sample1.csv" --get-line 3

This should print the contents of row 3 of the file to the screen.

## Bonus Points

Provide an option for saving some data into MongoDB

## Tips that might help you

* [Argparse for CLI - Intermediate Python Programming p.3](https://www.youtube.com/watch?v=0twL6MXCLdQ)
* [Writing awesome Command-Line Programs in Python](https://www.youtube.com/watch?v=gR73nLbbgqY&t)
* [Working with CSV files](https://www.youtube.com/watch?v=q5uM4VKywbA&feature=youtu.be)
* [Tutorial — PyMongo 3.5.1 documentation - MongoDB API](http://api.mongodb.com/python/current/tutorial.html)
