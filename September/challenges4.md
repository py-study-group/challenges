# Monthly programming challenges for the study.py group

## 1) Use Python to see who is connected your network

Get the local IP address and subnet mask and calculate the address range in your network segment. Scan all the addresses and display those that are alive.

### Bonus Points

Save the IP adresses to a textfile (.csv, .txt, .json, whatever you like)


## 2) Use named pipes to pass data between two Python scripts.

Create two scripts:

1. server.py

2. client.py

client.py uses a named pipe to send a text message to client.py.

server.py waits for the message and displays its contents.

On Linux you can use `os.mkfifo()` to work with named pipes and on Windows you can use Tim Golden's pywin32 module.

### Bonus Points

Create a class called `NamedPipe` that encapsulates working with named pipes. 

`NamedPipe.__init__()` method should accept one argument - the path of the named pipe (eg. '/tmp/mypipe' on Linux).

NamedPipe should have three methods: `read()`, `write()` and `close()`. Both `client.py` and `server.py` should use NamedPipe for communication.


## 3) Use pyaudio to generate and play a few tones of your favourite song

Each music note has a frequency. You can look up frequencies you need on [Wikipedia](https://en.wikipedia.org/wiki/C_(musical_note))

You can use pyaudio to generate tones of the specified frequency and play them. You can find an example [on stackoverflow](https://stackoverflow.com/questions/8299303/generating-sine-wave-sound-in-python?rq=1)

### Bonus Points

Calculate note frequencies from one starting frequency (eg. C note frequency)
Handy link: https://pages.mtu.edu/~suits/NoteFreqCalcs.html
