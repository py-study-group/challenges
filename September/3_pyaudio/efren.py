#!/usr/local/bin/python3

'''
This script plays notes

Contains classes for Notes and Music
'''

import argparse
import numpy
import os
import string
import sys
import time
import pyaudio

# Globals
VOLUME = 0.5
HIGH_A = 440
HIGH_A_KEY_POS = 49
DEFAULT_RATE = 44100

# Splitting one octave into 12 logarithmic, equally-spaced intervals
# means that each note frequency is equal to the frequency of the
# previous (lower) semitone multiplied by the 12th root of 2,
PITCH_SHIFT = 1.059463094359

# Below are the notes for the intro to "Iron Man" by Black Sabbath
# Each note is a tuple: (note, duration) and are relative to the HIGH_A
IRON_MAN_NOTES = [
    ("E3", 3.2),
    ("G3", 3.1),
    ("G3", 2.0),
    ("A3", 1.9),
    ("A3", 3.2),
    ("C4", 0.8),
    ("B3", 0.9),
    ("C4", 0.8),
    ("B3", 0.9),
    ("C4", 0.8),
    ("B3", 0.9),
    ("G3", 1.8),
    ("G3", 1.9),
    ("A3", 1.8),
    ("A3", 1.9),
]


class Note(object):
    '''A single note'''
    def __init__(self, step, duration, rate=DEFAULT_RATE):
        self.step = step
        self.duration = duration
        self.rate = rate

    @property
    def freq(self):
        '''Calculates frequency based on step'''
        return round(HIGH_A * numpy.power(PITCH_SHIFT, self.step), 1)

    @property
    def sample(self):
        '''Generate samples, note conversion to float32 array'''
        return (numpy.sin(2*numpy.pi*numpy.arange(self.rate*self.duration)*self.freq/self.rate)).astype(numpy.float32)


class Music(object):
    '''Music Handler that plays notes'''
    def __init__(self, notes=[], volume=VOLUME, adapter=pyaudio.PyAudio()):
        self.audio_adapter = adapter
        self.user_notes = notes
        self.volume = volume

    def play(self, channels=1):
        '''Plays notes'''
        for note in self.notes:
            stream = self.audio_adapter.open(
                format=pyaudio.paFloat32,
                channels=channels,
                rate=note.rate,
                output=True
            )
            stream.write(self.volume*note.sample)

    @property
    def keys(self):
        '''Returns a list of tuples of keys (same notes are tupled together)'''
        return [
            ("C"), ("C#", "Db"),
            ("D"), ("D#", "Eb"),
            ("E"),
            ("F"), ("F#", "Gb"),
            ("G"), ("G#", "Ab"),
            ("A"), ("A#", "Bb"),
            ("B")
        ]

    @property
    def notes(self):
        '''Map user's notes to steps'''
        try:
            notes = []
            for user_note in self.user_notes:
                # Get the step from note map
                note = Note(
                    step=self.note_map[user_note[0].upper()],
                    duration=user_note[1]
                )
                notes.append(note)
            return notes
        except KeyError as error:
            raise Exception("Note not found in map: {}".format(error))

    @property
    def note_map(self):
        '''Builds master note step map'''
        # Mapping is based on https://en.wikipedia.org/wiki/Piano_key_frequencies
        note_map = {}
        # Start at base key number to calculate for frequency
        key_pos = 1
        for octave in range(8):
            for notes in self.keys:
                added_note = False
                for note in notes:
                    if self.skip_note(note, octave):
                        # Skip adding note and bypass key_pos increment
                        continue
                    key = "{}{}".format(note, octave)
                    # Calculate position of note relative to constant
                    note_map[key] = key_pos - HIGH_A_KEY_POS
                    added_note = True
                if added_note:
                    # Compensate for next frequency
                    key_pos += 1
        return note_map

    @staticmethod
    def skip_note(note, octave):
        '''Return True if skipping key in mapping, False otherwise'''
        # The mapping will start with A0, A#/Bb0, B0 before going to C1
        # So C0-G0 (including sharps/flats therein) won't be mapped
        return note not in ["A", "A#", "Bb", "B"] and octave == 0


def main(args):
    if args.note:
        note = args.note
        if not note[-1].isdigit():
            note = '{}{}'.format(note, 4)
            print("No subscript provided. Playing '{}'".format(note))
        notes = [(note, args.duration)]
    else:
        # If no note is passed, play some Iron Man
        notes = IRON_MAN_NOTES
    music = Music(notes=notes, volume=args.volume)
    music.play()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Music/Note Player")
    parser.add_argument("-n", "--note", type=str, help="Note to play")
    parser.add_argument("-v", "--volume", type=float, help="Volume", default=VOLUME)
    parser.add_argument("-r", "--rate", help="Rate", default=DEFAULT_RATE)
    parser.add_argument("-d", "--duration", type=float, help="Duration", default=3)
    args = parser.parse_args()
    try:
        main(args)
    except Exception as error:
        print(str(error))
