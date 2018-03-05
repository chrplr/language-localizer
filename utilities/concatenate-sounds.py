#! /usr/bin/env python3
# Time-stamp: <2018-02-26 20:09:03 cp983411>

"""
Given a textfile containing words for which wav files already exist in the current directory, generate a sound file for each line as the concatenation of the individual words.
"""

import sys

from typing import List
from unidecode import unidecode  # to remove accents
from pydub import AudioSegment


def detect_leading_silence(sound: AudioSegment,
                           silence_threshold=-50.0,  # in dB
                           chunk_size=10) -> int:
    '''
    returns the number of ms containing silence at the beginning of sound
    '''
    trim_ms = 0  # ms
    assert chunk_size > 0  # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold:
        trim_ms += chunk_size
        if trim_ms > len(sound):
            trim_ms = len(sound)
            break
    return trim_ms


def trim(sound: AudioSegment) -> AudioSegment:
    """ remove silence at the beginning and end of sound """
    start_trim = detect_leading_silence(sound)
    end_trim = detect_leading_silence(sound.reverse())
    duration = len(sound)
    return sound[start_trim:duration-end_trim]


def concat(sounds: List[AudioSegment], gap=0) -> AudioSegment:
    """ concatenate a series of sounds, inserting 'gap' ms of silence between them """
    sum = AudioSegment.empty()
    sil = AudioSegment.silent(duration=gap)
    for s in sounds:
        sum += trim(s) + sil  # TODO: prevent sil from being added also added at the end
    return sum


def main(textfile: str, gap: int, prefix: str):
    with open(textfile) as infile:
        for (i, phrase) in enumerate(infile.read().splitlines()):
            audio_in = [AudioSegment.from_file(unidecode(w) + '.wav', format='wav') for w in phrase.split()]
            audio_out = concat(audio_in, gap)
            fn = "{}{:03d}.wav".format(prefix, i + 1)
            audio_out.export(fn, format='wav')


def usage():
    print(sys.argv[0] + ' textfile gap prefix')
    print("Given 'textfile' containing words for which wav files already exist in the current directory, generate a sound file (with name starting with 'prefix') for each line as the concatenation of the individual words on the line, with 'gap' milliseconds of slience betwen them.")
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        usage()
    main(sys.argv[1], int(sys.argv[2]), sys.argv[3])
