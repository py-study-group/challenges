#!/usr/bin/env python3

import sys

import enchant


class NothingLooksRightError(Exception):
    pass


class Caesar:
    """
    This makes a number of assumptions:

    1. Only letters wrap in the cipher.  This means that other forms of
       punctuation, including spaces, quotes and brackets won't be shifted.
    2. We assume that we're expecting an English-language message, though this
       can be adjusted by change the value of ``DICTIONARY``.  For that matter,
       we also assume an ASCII character set.  I suppose this could be adapted
       though with some arguments to ``__init__()``.
    3. We assume that the file, once decoded anyway, is correctly spelt.

    Try this with input that looks like this:

      Uijt jt uif tpoh uibu epfto'u foe, boe ju hpft po boe po nz gsjfoe ;-)
    """

    UPPER = list(range(ord("A"), ord("Z") + 1))
    LOWER = list(range(ord("a"), ord("z") + 1))
    LETTERS = [chr(_) for _ in UPPER + LOWER]
    WORD_CHARACTERS = LETTERS + [" ", "'"]

    DICTIONARY = enchant.Dict("en_GB")

    def encode(self, raw, shift):
        """
        Given some text, attempt to encode it with a shift value of ``shift``.
        """
        return self._shift_string(raw, shift)

    def decode(self, raw):
        """
        Given a bunch of (presumably) encoded text, attempt to guest the Caesar
        shift value and then decode it.
        """
        return self._shift_string(raw, self._guess_shift(raw))

    def _get_shifted(self, c, shift):
        """
        Given a character, return the result of shifting that character shifted
        by ``shift``
        """

        letter_set = self.LOWER
        if c.upper() == c:
            letter_set = self.UPPER

        return chr(letter_set[letter_set.index(ord(c)) - shift])

    def _shift_string(self, raw, shift):
        """
        Given an encoded string and a shift value, shift all shiftable
        characters and return the result.
        """

        r = ""
        for c in list(raw):
            if c in self.LETTERS:
                r += self._get_shifted(c, shift)
                continue
            r += c

        return r

    def _guess_shift(self, raw):
        """
        Increment the shift until the text looks like the language we're
        expecting.
        """

        sanitised_raw = "".join(
            [_ for _ in raw if _ and _ in self.WORD_CHARACTERS])

        for shift in range(26):
            if self._looks_like_english(sanitised_raw, shift):
                return shift

        raise NothingLooksRightError()

    def _looks_like_english(self, raw, shift):
        """
        Check the spelling of each word, and if everything is perfect, assume
        that this string is legit.
        """
        for word in self._shift_string(raw, shift).lower().split(" "):
            if word and not self.DICTIONARY.check(word):
                return False
        return True


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(Caesar().decode(f.read()))
