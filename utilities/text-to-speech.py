# /usr/bin/env python
#  -*- coding: utf-8 -*-
# Time-stamp: <2018-03-05 16:21:12 cp983411>

"""
This script creates a DOS batch script to synthesize lines of words listed in a file. The synthesizer is [balabolka](http://www.cross-plus-a.com/balabolka.htm)
"""

import os.path as op

dir = '/Users/Philippine/Downloads/balcon/'
fn = 'Phrases_Set8.txt'
fo = 'phrases_s8'


liste = open(op.join(dir, fn))
ph = 1

cmds = open(op.join(dir, 'creewav.bat'), 'w')
for i in liste.readlines():
    phrase = i.rstrip()
    if len(phrase) > 0:
        outfn = fo + "_%03d.txt" % ph
        out = open(op.join(dir, outfn), 'w')
        out.write(phrase)
        out.close()
        outfnwav = fo + "_%03d.wav" % ph
        cmds.write('balcon -f %s -w %s\n' % (outfn, outfnwav))

        # Synthesize each word indivudally
        # for w in phrase.split():
        #     cmds.write('balcon -t ' + w + ' -w ' + w + '.wav\n')

        ph += 1
cmds.close()
