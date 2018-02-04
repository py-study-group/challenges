#!/usr/bin/env python
"""
February Challenge - PyStudyGroup

Take a string or text file as input, and encode/decode it with a Caesarian
cipher by any amount of shift.

ABCDEF...XYZ

shifted by +3 characters becomes...

DEFGHI...ABC

"""

import click
import string
import os

scriptDirectory = os.path.dirname(os.path.realpath(__file__))

# Create set of real English words
with open(os.path.join(scriptDirectory, "english_words.txt")) as word_file:
    english_words = set(word.strip().lower() for word in word_file)


def is_english_word(word):
    return(word.lower() in english_words)


def shift_text(unshifted_text, encoding, shift):
    """ Perform Caesarian cipher shift. If decoding, simply reverse the parity of the shift amount."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    unshifted_text = unshifted_text.upper()

    if encoding == "decode":
        shift *= -1

    shifted_text = ''.join(
        [alphabet[(alphabet.index(letter) + shift) % 26] if letter in alphabet else letter for letter in unshifted_text])
    return(shifted_text)


def real_word_freq(decoded_text):
    """ Return dict of frequencies of all English words present in input text."""
    real_word_freqs = {}
    table = str.maketrans({key: None for key in string.punctuation})
    cleaned_text = decoded_text.translate(table)
    for word in cleaned_text.split(' '):
        if is_english_word(word):
            if word not in real_word_freqs:
                real_word_freqs[word] = 1
            else:
                real_word_freqs[word] += 1
    return(real_word_freqs)


def percent_real_words(decoded_text):
    """ Return total number of real words present in input text."""
    table = str.maketrans({key: None for key in string.punctuation})
    cleaned_text = decoded_text.translate(table)
    return(sum(real_word_freq(decoded_text).values()) / len(cleaned_text.split(' ')))


def auto_decode(unshifted_text):
    """ Get word frequencies for each real English word for each cipher shift amount, then the shift
    with the maximum ratio of real words to all words is returned."""
    cipher_quality = {shift: percent_real_words(shift_text(
        unshifted_text, "decode", shift)) for shift in range(1, 26)}
    return(int(max(cipher_quality, key=cipher_quality.get)))


@click.command()
@click.argument('encoding', type=str, required=False)
@click.argument('shift', type=int, required=False)
@click.option('--auto', '-a', is_flag=True, help="Automatically try to decode text, returns decoded text and shift amount, or -1 if it cannot determine an appropriate cipher shift.")
@click.option('--file', '-f', default=None, required=False, help="The path to a text file to encode/decode.",)
@click.option('--text', '-t', default=None, required=False, help="Raw text to encode/decode.",)
def main(encoding, shift, auto, file, text):
    """
    A tool for performing a Caesarian shift cipher on a string or text file.

    Permits encode/decode by a nonnegative integer shift value, and automatic decode that returns the most likely shift value to return English text.
    """

    if not auto:
        if encoding not in ["encode", "decode"]:
            print("Must specify ""encode"" or ""decode"".")
            return()
        if not isinstance(shift, int):
            print(
                "If using encode/decode, must supply a non-negative integer value to shift.")
            return()
        if not file and not text:
            unshifted_text = click.prompt(
                "Please enter text to be {}d.".format(encoding), default="")
        else:
            if file:
                with open(file) as inputfile:
                    unshifted_text = inputfile.read()
            if text:
                unshifted_text = text

        shifted_text = shift_text(unshifted_text, encoding, shift)
        print(shifted_text)
        return(shifted_text)

    else:
        unshifted_text = text
        autoshift = auto_decode(unshifted_text)
        if autoshift == 1:
            print("Decoding with a shift of 1 character leads to decrypted text most resembling English.".format(
                autoshift))
        else:
            print("Decoding with a shift of {} characters leads to decrypted text most resembling English.".format(
                autoshift))
        decoded_text = shift_text(unshifted_text, "decode", autoshift)
        print("Preview : \"{}\"".format(decoded_text[:100] + " ..." if len(decoded_text)
                                        > 100 else decoded_text))
        return(autoshift)

if __name__ == "__main__":
    main()
