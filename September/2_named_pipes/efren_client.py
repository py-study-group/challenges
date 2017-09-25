#!/usr/local/bin/python3

'''
This file is the client that will send
data into the named pipe

This accepts argument for message. Wrap message
in quotes if needed (more than one word).

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
    print("Sending {} to pipe.".format(args.message))
    named_pipe = NamedPipe(args.pipe)
    named_pipe.write(args.message)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Name Pipe Client")
    parser.add_argument("message", type=str, help="Message to send")
    parser.add_argument("-p", "--pipe", help="Pipe full path", default=DEFAULT_PIPE_NAME)
    args = parser.parse_args()
    main(args)
