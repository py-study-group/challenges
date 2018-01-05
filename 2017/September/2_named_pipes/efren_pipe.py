'''
This file contains NamedPipe object
'''

import os

DEFAULT_PIPE_NAME = "/tmp/fifo_challenge.txt"


class NamedPipe(object):
    '''Named Pipe Object Handler Class'''
    def __init__(self, pipe):
        self.pipe = pipe

    def read(self):
        '''Read from pipe and yield result'''
        file_handler = open(self.pipe, "r")
        for line in file_handler:
            yield line
        self.close(file_handler, True)

    def write(self, message):
        '''Write to named pipe'''
        self._init_pipe()
        file_handler = open(self.pipe, "w")
        file_handler.write("{}\n".format(message))
        self.close(file_handler)

    def close(self, file_handler, remove_file=False):
        '''Close named pipe'''
        file_handler.close()
        if remove_file:
            os.remove(self.pipe)

    def _init_pipe(self):
        '''Initializes named pipe'''
        try:
            os.mkfifo(self.pipe)
        except FileExistsError as error:
            # In the event the file exists, remove it
            os.remove(self.pipe)
            self._init_pipe()
