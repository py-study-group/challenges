#!/opt/anaconda/bin/python
"""Script co chack whether an e-mail adress is valid."""

import argparse
import re


def main():
    """Main program routine."""
    # Get the string
    args = create_parser()
    string = args.mail
    # Check validity
    valid = check_validity(string)
    # Print results
    print_result(valid)
    pass


def create_parser():
    """Create the argparser."""
    parser = argparse.ArgumentParser()
    # Argument for E-Mail string
    parser.add_argument('mail', type=str,
                        help="The String to check for validity.")
    return parser.parse_args()


def check_validity(mail):
    """Check if the string is a valid E-mail via regex."""
    result = re.search(r'^.*@{1}.*\.{1}.*\.?.*$', mail)
    if result:
        return True
    else:
        return False


def print_result(validity):
    """Print the result to stdout."""
    if validity:
        print("This is a valid e-mail adress.")
    else:
        print("Invalid E-Mail adress.")


if __name__ == '__main__':
    main()