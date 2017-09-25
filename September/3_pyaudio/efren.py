#!/usr/local/bin/python3

'''
This file plays notes

Contains classes for Notes and AudioHandler
'''

import numpy
import os
import sys
import time
import pyaudio

# Globals
BASE_NOTE=440           # Default is 440 (which is A4)
DEFAULT_FREQUENCY=44100

# Splitting one octave into 12 logarithmic, equally-spaced intervals
# means that each note frequency is equal to the frequency of the
# previous (lower) semitone multiplied by the 12th root of 2,
PITCH_SHIFT = 1.059463094359

# Below are the notes for the intro to "Iron Man" by Black Sabbath
# Each note or "step" is a tuple containing:
#       (step, volume, and duration)
# These are relative to the BASE_NOTE
# Ideally, these should be music notes but perhaps that's for a rainy day!
IRON_MAN = [
    (-17, 0.5, 3.2),
    (-14, 0.5, 3.1),
    (-14, 0.5, 2.0),
    (-12, 0.5, 1.9),
    (-12, 0.5, 3.2),
    (-9, 0.5, 0.8),
    (-10, 0.5, 0.9),
    (-9, 0.5, 0.8),
    (-10, 0.5, 0.9),
    (-9, 0.5, 0.8),
    (-10, 0.5, 0.9),
    (-14, 0.5, 1.8),
    (-14, 0.5, 1.9),
    (-12, 0.5, 1.8),
    (-12, 0.5, 1.9),
]


class Note(object):
    '''A single note'''
    def __init__(self, step, volume, duration, rate=DEFAULT_FREQUENCY):
        self.step = step
        self.volume = volume
        self.duration = duration
        self.rate = rate

    @property
    def freq(self, base=BASE_NOTE):
        '''Calculates frequency based on step'''
        return round(base * numpy.power(PITCH_SHIFT, self.step), 1)

    @property
    def sample(self):
        '''Generate samples, note conversion to float32 array'''
        return (numpy.sin(2*numpy.pi*numpy.arange(self.rate*self.duration)*self.freq/self.rate)).astype(numpy.float32)


class Music(object):
    '''Music Handler that plays notes'''
    def __init__(self, steps=[], adapter=pyaudio.PyAudio()):
        self.audio_adapter = adapter
        self.steps = steps

    def play(self, channels=1):
        '''Plays notes'''
        for note in self.notes:
            stream = self.audio_adapter.open(
                format=pyaudio.paFloat32,
                channels=channels,
                rate=note.rate,
                output=True
            )

            stream.write(note.volume*note.sample)

    @property
    def notes(self):
        '''Calculates notes from steps'''
        notes = []
        for st in self.steps:
            note = Note(
                step=st[0],
                volume=st[1],
                duration=st[2]
            )
            notes.append(note)
        return notes


def main(notes):
    music = Music(notes)
    music.play()


if __name__ == "__main__":
    notes = IRON_MAN
    main(notes)
