#! /usr/bin/env python
# Time-stamp: <2015-04-21 17:00 christophe@pallier.org>

"""
Demo script for the syntcomp experiment

christophe@pallier.org
"""

# FONT = 'fonts/Inconsolata.ttf'
FONT = "fonts/TITUSCBZ.TTF"
FONT_SIZE = 36

SOA = 200   # stimulus onset asynchrony (=time of display of a string)
BLOCDURATION = SOA * 34  
NBLOCKS = 24
INITIALWAIT = 3000
BETWEEN_BLOCS = 8000
TOTAL_DURATION = INITIALWAIT + (BLOCDURATION + BETWEEN_BLOCS) * NBLOCKS

import sys
import csv
import os
import expyriment
from expyriment import design, control, stimuli, io


#%%

exp = design.Experiment(name="Visual Language Localizer")

# comment out the following line to get in real mode
# control.set_develop_mode(True)

control.initialize(exp)

#%%

control.start(exp)

fixcross = stimuli.FixCross(size=(30, 30), line_width=3, colour=(0, 255, 0))
fixcross.preload()

fixcross2 = stimuli.FixCross(size=(30, 30), line_width=2, colour=(128, 128, 128))
fixcross2.preload()

liste = "list%d.csv" % (2 - exp.subject % 2)
listname = os.path.join("lists", liste)


sequences = [i for i in csv.reader(open(listname))]

block = design.Block(name="block1")

for line in sequences:
    trial = design.Trial()
    trial.set_factor("Condition", line[0])
    stim = []
    for w in line[1:]:
        if sys.version_info > (3, 0):
            s = w
        else:
            s = w.decode('utf-8')
        stim = stimuli.TextLine(s, text_font=FONT, text_size=FONT_SIZE)
        trial.add_stimulus(stim)

    block.add_trial(trial)

exp.add_block(block)
exp.data_variable_names = ["Condition", "Onset", "Duration"]

#%%

for block in exp.blocks:
    fixcross.present()
    exp.keyboard.wait_char('t')  # wait_for_MRI_synchro()
    exp.screen.clear()
    exp.screen.update()

    t0 = expyriment.misc.Clock()
    exp.clock.wait(INITIALWAIT - 1000)

    for n, trial in enumerate(block.trials):
        for stim in trial.stimuli:
            stim.preload()

        while t0.time < (INITIALWAIT + n * (BLOCDURATION + BETWEEN_BLOCS) - 800):
            exp.clock.wait(10)
            io.Keyboard.process_control_keys()

        exp.clock.wait(600 - fixcross2.present())
        exp.screen.clear()
        exp.screen.update()

        while t0.time < (INITIALWAIT + n * (BLOCDURATION + BETWEEN_BLOCS)):
            exp.clock.wait(10)
            io.Keyboard.process_control_keys()
        onset = t0.time

        for stim in trial.stimuli:
            exp.clock.wait(SOA - stim.present())

        duration = t0.time - onset
        exp.data.add([trial.get_factor("Condition"), onset, duration])

        exp.screen.clear()
        exp.screen.update()

        io.Keyboard.process_control_keys()

exp.clock.wait(8000)
print("Duration = %dmsec", t0.time)
control.end()
