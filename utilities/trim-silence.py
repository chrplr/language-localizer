#! /usr/bin/env python

# stolen from https://stackoverflow.com/questions/29547218/remove-silence-at-the-beginning-and-at-the-end-of-wave-files-with-pydub

import sys

from pydub import AudioSegment

def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=10):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms

    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0 # ms

    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms


if __name__ == '__main__':
    for f in sys.argv[1:]:
        sound = AudioSegment.from_file(f, format="wav")

        start_trim = detect_leading_silence(sound)
        end_trim = detect_leading_silence(sound.reverse())

        duration = len(sound)
        trimmed_sound = sound[start_trim:duration-end_trim]

        trimmed_sound.export(f, format='wav')


