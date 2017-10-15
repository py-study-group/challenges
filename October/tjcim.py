""" Process CSV Files """
import os
import sys
import csv
import argparse
import logging.config

import requests


LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'tjcim_formatter': {
            'format': '[{levelname}][{name}] {message}',
            'style': '{',
        },
    },
    'handlers': {
        'consoleHandler': {
            'class': 'logging.StreamHandler',
            'formatter': 'tjcim_formatter',
        },
    },
    'loggers': {
        'tjcim': {
            'handlers': ['consoleHandler'],
            'level': 'INFO',
        },
    },
}
logging.config.dictConfig(LOGGING_CONFIG)
log = logging.getLogger("tjcim")


def download_csv_file_to_list(url):
    """ Given a URL to a csv file this will download it and return a list with its contents. """
    # Download file
    try:
        with requests.Session() as session:
            download = session.get(url)
    except:
        log.error("Error downloading from url {}".format(url))
        raise SystemExit
    decoded = download.content.decode('utf-8')
    results = stream_to_list(decoded)
    return results


def stream_to_list(stream):
    """ Convert stream to list. """
    csv_reader = csv.reader(
        stream.splitlines(),
        skipinitialspace=True,
    )
    rows = []
    try:
        for row in csv_reader:
            if row:
                rows.append(row)
        return rows
    except ValueError as e:
        log.error('Malformed csvfile: {}'.format(e))
        raise SystemExit


def csv_to_list(in_file):
    """ Read a csv file and return the rows as a python list. """
    if not os.path.isfile(in_file):
        log.error("File doesn't exist: {}".format(in_file))
        raise SystemExit
    results = []
    with open(in_file, 'r') as a_csv:
        results = stream_to_list(a_csv.read())
    return results


def write_list_to_csv(in_list, out_file):
    """ This will write the list to the out_file. """
    with open(out_file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(in_list)


def get_line(line_number, csv_list):
    """ return the contents of the csv_file at the specified line_number as a python list. """
    try:
        if not line_number > 0:
            log.error("The provided line_number: {} is incorrect.".format(line_number))
            return None
    except TypeError:
        log.error("line_number must be an integer.")
        return None
    try:
        results = csv_list[line_number - 1]
    except IndexError:
        log.error("The list does not contain {} lines.".format(line_number))
        return None
    return [results]


def remove_line(line_number, csv_list):
    """ return the contents of csv_list without the specified line_number. """
    try:
        if not line_number > 0:
            log.error("The provided line_number: {} is incorrect.".format(line_number))
            return None
    except TypeError:
        log.error("line_number must be an integer.")
        return None
    try:
        del csv_list[line_number - 1]
    except IndexError:
        log.error("The list does not contain {} lines.".format(line_number))
        return None
    return csv_list


def filter_list(filter_text, csv_list):
    """ Filter the contents of csv_list returning only those that have a filter_text in the row."""
    matched = []
    for row in csv_list:
        if filter_text in row:
            matched.append(row)
            log.debug("Found matching rows: {}.".format(row))
    if matched:
        return matched
    else:
        log.debug("Did not find any rows containing {}".format(filter_text))
        matched.append("Nothing found.")


def merge_all_files(csv_files):
    """ Merge csv files into a list. """
    results = []
    for csv_file in csv_files:
        new_list = csv_to_list(csv_file)
        results = results + new_list
    return results


def main(args):
    """ Process the CSV files. """
    # Get a list from input.
    if args.file:
        log.debug("Processing file {}.".format(args.file))
        contents = csv_to_list(args.file)
    elif args.http_get_file:
        log.debug("Processing http {}.".format(args.http_get_file))
        contents = download_csv_file_to_list(args.http_get_file)
    else:
        log.debug("Processing merge {}.".format(args.merge))
        contents = merge_all_files(args.merge)

    # Take action
    action = False
    results = []
    if args.get_line:
        log.debug("Getting line {}.".format(args.get_line))
        results = get_line(args.get_line, contents)
        action = True
    elif args.remove_line:
        log.debug("Removing line {}.".format(args.get_line))
        results = remove_line(args.remove_line, contents)
        action = True
    elif args.filter:
        log.debug("Filtering file for {}.".format(args.filter))
        results = filter_list(args.filter, contents)
        action = True
    else:
        log.debug("Taking no action.")

    # Output
    if args.output_file:
        log.debug("Saving file.")
        write_list_to_csv(results if action else contents, args.output_file)
    else:
        log.debug("Printing results:")
        print_out = results if action else contents
        print("\r\n" + "*" * 10 + " Results " + "*" * 10 + "\r\n")
        for row in print_out:
            print(row)


def parse_args(args):
    """ Parse the command line arguments """
    # Merge file cannot
    parser = argparse.ArgumentParser(prog='tjcim.py', description='Process CSV files.')
    parser.add_argument('--output-file', help='Save processed CSV file here')
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('--file', help='CSV File to Process')
    input_group.add_argument('--http-get-file', help='URL of CSV file to download and process.')
    input_group.add_argument('--merge', nargs='+',
                             help='Space seperated list of two or more files to merge')
    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument('--get-line', type=int, help='Returns file line of given line-number')
    action_group.add_argument(
        '--remove-line', type=int, help='Removes file line of given line-number')
    action_group.add_argument('--filter', help='Returns all lines containing these words.')
    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument('--verbose', '-v', action='store_true', required=False,
                                 help="Log debug to screen.")
    verbosity_group.add_argument('--quiet', '-q', action='store_true', required=False,
                                 help='Script will only output errors.')
    args = parser.parse_args(args)
    if args.merge and len(args.merge) < 2:
        log.error("Merge provided with only one file. You must provide two or more.")
        raise SystemExit
    logger = logging.getLogger("tjcim")
    if args.quiet:
        logger.setLevel('ERROR')
    elif args.verbose:
        logger.setLevel('DEBUG')
    else:
        logger.setLevel('INFO')
    return args


if __name__ == '__main__':
    main(parse_args(sys.argv[1:]))
