#!/usr/local/bin/python3
#
# Monthly programming challenges for the study.py group. This solution uses a class structure.
#
# Use named pipes to pass data between two Python scripts.
#
# Create two scripts: server.py and client.py
#
# client.py uses a named pipe to send a text message to client.py.
# server.py waits for the message and displays its contents.
#
# On Linux you can use os.mkfifo() to work with named pipes and on Windows you can use Tim Golden's pywin32 module.
#
# Bonus Points
#
# Create a class called NamedPipe that encapsulates working with named pipes.
# NamedPipe.__init__() method should accept one argument - the path of the named pipe(eg. '/tmp/mypipe' on Linux).
# NamedPipe should have three methods: read(), write() and close(). Both client.py and server.py should use NamedPipe for communication.
#
#
#  >>>>>>>>> NOTE <<<<<<<<<
#
# I decided to do things a little differently from the requirement- instead I used one script with
# arguemnts passed in to choose the server or client functionality and had the server loop until ^C
# was pressed. My motivation was (mostly) to continue to get experience with argparse and get familiar
# with signal processing.
#
# Author: Chad Lake (https://github.com/lackhead)
#


###############################################
# Dependencies                                #
###############################################
import argparse
import errno
import os
import signal
import stat
import sys


###############################################
# Classes                                     #
###############################################
class NamedPipe():

    def __init__(self, filename):
        self.filename = str(filename)
        self.FIFO = ""

    def __repr__(self):
        return 'NamedPipe({})'.format(self.filename)

    def __enter__(self):
        return self

    def __exit__(self, *Args):
        if self.FIFO:
            self.FIFO.close()
        # try to remove the pipe
        try:
            os.unlink(self.filename)
        except OSError as oe:
            if oe.errno != errno.ENOENT:
                raise

    def read(self):
        # create the pipe if necessary
        try:
            os.mkfifo(self.filename)
        except OSError as oe:
            if oe.errno != errno.EEXIST:
                raise
        # open it up for reading if necessary
        if not self.FIFO:
            self.FIFO = open(self.filename)
        # read and return
        return self.FIFO.read().strip()

    def write(self, msg):
        # create the pipe if necessary
        try:
            os.mkfifo(self.filename)
        except OSError as oe:
            if oe.errno != errno.EEXIST:
                raise
        # open it up for reading if necessary
        if not self.FIFO:
             self.FIFO = open(self.filename, 'w')
        print(msg, file=self.FIFO)


###############################################
# Functions                                   #
###############################################

def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, OriginalSigint)

    # try to remove the pipe
    try:
        os.unlink(Args.file)
    except OSError as oe:
        if oe.errno != errno.ENOENT:
            # re-raise unless the file doesn't exist
            raise

    # and we're out of here
    sys.exit()


###############################################
# Deal with arguments                         #
###############################################

Parser = argparse.ArgumentParser(description="Send a message between two processes using named pipes")
Parser.add_argument("-m", "--message", help="the message to send to the server")
Parser.add_argument("-s", "--server", action='store_true', help="act as server (receive messages)")
Parser.add_argument("-f", "--file", help="the file that specifies the named pipe", required=True)
Args = Parser.parse_args()

# either -c or -s must be specified, but not both
if (Args.message and Args.server):
    print("You must use either -s or -m, not both")
    sys.exit(1)
elif ((not Args.message) and (not Args.server)):
    print("You must specify one of the following: -s or -c")
    sys.exit(1)


###############################################
# Server functionality                        #
###############################################
# server should open the file for reading
# and loop reading and outputting until ^D
if (Args.server):

    # keep looping and printing until ^C is hit
    print("Hit ^C to quit the server")
    # Save the original interrupt
    OriginalSigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)

    # Use a loop to wait on opening the pipe
    # then read whatever we can and echo it
    # close the pipe
    print("Listening...", flush=True)
    while True:
        with NamedPipe(Args.file) as MyNamedPipe:
            print("Message received: {}".format(MyNamedPipe.read()))


###############################################
# Client Functionality                        #
###############################################
if (Args.message):
    # simple- just print out the message
    with NamedPipe(Args.file) as MyNamedPipe:
        MyNamedPipe.write(Args.message)
