#! /usr/bin/env python

'''
    https://github.com/py-study-group/challenges/blob/master/October/challenge.md
    sam.i.am        .py - Uses argparse to get information from csv files.
    Use october_study_argparse -h to see the help menu.
'''
import argparse
import csv
import requests


class FileParser():

    def __init__(self, file, get_line, remove_line, filter,
                 output_file, http_get_file, merge_files):
        self.file = file
        self.get_line = get_line
        self.remove_line = remove_line
        self.filter = filter
        self.output_file = output_file
        self.http_get_file = http_get_file
        self.merge_files = merge_files

    def file_get_line(self, file, get_line):
        ''' Given file location, prints the line from csv file '''
        with open(file) as infile:
            in_reader = csv.reader(infile)
            for row in in_reader:
                if in_reader.line_num == get_line:
                    print(row)

    def file_remove_line(self, file, remove_line, output_file):
        ''' Prints line removed or writes to output file'''
        if output_file:
            with open(file, 'r') as infile:
                in_reader = csv.reader(infile)
                with open(output_file, 'w') as outfile:
                    out_writer = csv.writer(outfile)
                    for row in in_reader:
                        if in_reader.line_num == remove_line:
                            out_writer.writerow(row)
        else:
            with open(file, 'r') as infile:
                in_reader = csv.reader(infile)
                for row in in_reader:
                    if in_reader.line_num == remove_line:
                        print(row)

    def file_filter(self, file, filter, output_file):
        ''' Prints filtered word or writes to output file '''
        if output_file:
            with open(file, 'r') as infile:
                in_reader = csv.reader(infile)
                with open(output_file, 'w') as outfile:
                    out_writer = csv.writer(outfile)
                    for row in in_reader:
                        for word in row:
                            if word == filter:
                                out_writer.writerow([word])
        else:
            with open(file, 'r') as infile:
                in_reader = csv.reader(infile)
                for row in in_reader:
                    for word in row:
                        if word == filter:
                            print(word)

    def http_get_line(self, http_get_file, get_line):
        with open(http_get_file) as infile:
            in_reader = csv.reader(infile)
            for row in in_reader:
                if in_reader.line_num == get_line:
                    print(row)

    def http_remove_line(self, http_get_file, remove_line):
        ''' Given file's http address prints line from csv file '''
        list_infile = []
        with open(http_get_file) as infile:
            in_reader = csv.reader(infile)
            with open('outfile.csv', 'w') as outfile:
                out_writer = csv.writer(outfile)
                for row in in_reader:
                    if in_reader.line_num == args.remove_line:
                        continue
                    else:
                        list_infile.append(row)
                for row in list_infile:
                    out_writer.writerow(row)

    def http_filter(self, http_get_file, filter, output_file):
        ''' Prints filtered 'word' or writes to output file  '''
        with open(http_get_file) as infile:
            in_reader = csv.reader(infile)
            if args.output_file:
                with open(args.output_file, 'w') as outfile:
                    out_writer = csv.writer(outfile)
                    for row in in_reader:
                        for word in row:
                            if word == args.filter:
                                out_writer.writerow([word])
            else:
                for row in in_reader:
                    for word in row:
                        if word == args.filter:
                            print(word)

    def merge_get_line(self, merge_files, get_line):
        ''' Accepts multiple file locations to print a desired line'''
        files = merge_files
        for file in files:
            with open(file) as infile:
                in_reader = csv.reader(infile)
                for row in in_reader:
                    if in_reader.line_num == get_line:
                        print(row)

    def merge_remove_line(self, merge_files, remove_line, output_file):
        ''' Removes line number from multiple files and writes to output file'''
        files = merge_files
        if output_file:
            for file in files:
                infile = open(file, 'r')
                in_reader = csv.reader(infile)
                outfile = open(output_file, 'w')
                out_writer = csv.writer(outfile)
                for row in in_reader:
                    if in_reader.line_num == remove_line:
                        out_writer.writerow(row)
            infile.close()
            outfile.close()
        else:
            for file in files:
                infile = open(file, 'r')
                in_reader = csv.reader(infile)
                for row in in_reader:
                    if in_reader.line_num == remove_line:
                        print(row)
            infile.close()

    def merge_filter(self, merge_files, filter, output_file):
        ''' Filter out the 'word' from multiple file inputs'''
        files = merge_files
        if output_file:
            for file in files:
                infile = open(file, 'r')
                in_reader = csv.reader(infile)
                outfile = open(output_file, 'w')
                out_writer = csv.writer(outfile)
                for row in in_reader:
                    for word in row:
                        if word == filter:
                            out_writer.writerow([word])
            infile.close()
            outfile.close()
        else:
            for file in files:
                infile = open(file, 'r')
                in_reader = csv.reader(infile)
                for row in in_reader:
                    for word in row:
                        if word == filter:
                            print(word)
            infile.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        '--file', help=" enter file name '/home/user/folder/sample.csv'")
    group.add_argument('--http-get-file',
                       help="address format in http://www.something.com")
    group.add_argument('--merge-files', nargs='*',
                       help="you can enter multiple files 'sample1.csv sample2.csv'")

    parser.add_argument('--get-line', type=int,
                        help='the line number to be displayed')
    parser.add_argument('--remove-line', type=int,
                        help='line number to be removed')
    parser.add_argument('--filter', help="type the 'word' to be filtered out")
    parser.add_argument(
        '--output-file', help="the name the '/home/user/folder/output.csv' to be written")

    args = parser.parse_args()
    args_dict = vars(args)

    shell = FileParser(args.file, args.get_line, args.remove_line, args.filter,
                       args.output_file, args.http_get_file, args.merge_files)

    if args_dict['http_get_file']:
        # Requests library scrapes
        r = requests.get(args_dict['http_get_file'])
        r.encoding = 'utf-8'
        content = r.text
        with open('http_data.csv', 'w') as outfile:
            outfile.write(content)
        args_dict['http_get_file'] = 'http_data.csv'
        # --http flag actions
        if args_dict['get_line']:
            shell.http_get_line(
                args_dict['http_get_file'], args_dict['get_line'])
        elif args_dict['remove_line']:
            shell.http_remove_line(
                args_dict['http_get_file'], args_dict['remove_line'])
        elif args_dict['filter']:
            shell.http_filter(args_dict['http_get_file'], args_dict[
                              'filter'], args_dict['output_file'])
        # --file flag actions
    elif args_dict['file']:
        if args_dict['filter']:
            shell.file_filter(args_dict['file'], args_dict[
                              'filter'], args_dict['output_file'])
        elif args_dict['remove_line']:
            shell.file_remove_line(args_dict['file'], args_dict[
                                   'remove_line'], args_dict['output_file'])
        elif args_dict['get_line']:
            shell.file_get_line(args_dict['file'], args_dict['get_line'])
        # --merge flag actions
    elif args_dict['merge_files']:
        if args_dict['get_line']:
            shell.merge_get_line(
                args_dict['merge_files'], args_dict['get_line'])
        if args_dict['remove_line']:
            shell.merge_remove_line(args_dict['merge_files'], args_dict[
                                    'remove_line'], args_dict['output_file'])
        if args_dict['filter']:
            shell.merge_filter(args_dict['merge_files'], args_dict[
                               'filter'], args_dict['output_file'])
