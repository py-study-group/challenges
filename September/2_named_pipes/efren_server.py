#!/usr/local/bin/python3

'''
This file is the server that will consume
data from a named pipe

Optional param for pipe path
'''

import argparse
import os
import sys
from efren_pipe import (
    DEFAULT_PIPE_NAME,
    NamedPipe
)


def main(args):
    try:
        print("Reading from {}...".format(args.pipe))
        named_pipe = NamedPipe(args.pipe)
        for line in named_pipe.read():
            print("{}\n".format(line))
    except FileNotFoundError as error:
        print("{} does not exist.".format(args.pipe))
        sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Named Pipe Server")
    parser.add_argument("-p", "--pipe", help="Pipe full path", default=DEFAULT_PIPE_NAME)
    args = parser.parse_args()
    main(args)
