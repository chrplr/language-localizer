Simple language localizer for fMRI
==========================================


Sentences are read from a csv file and displayed using Rapid Serial Visual Presentation. 

Beside a Python interpreter, you will need:

- the Python package [expyriment](http://expyriment.org) (usually installed by `pip install expyriment`)

- to obtain the font file `TITUSCBZ.TTF` from the page
http://titus.fkidg1.uni-frankfurt.de/unicode/tituut.asp

- Copy `TITUSCBZ.TTF` to the same directory as `langloc.py`

Then, to run the experiment, type:

     python langloc-visual.py 

When you see 'Ready', press the space bar.
When you see the green cross, press 't' to launch the experiment.

You can interrupt the script at any time by pressing ESC.

To run full screen, change the line

    control.set_develop_mode(True)
    
into

    control.set_develop_mode(False)


The experimental list (list1.csv or list2.csv in french_lists) is selected on the basis of the parity of the subject's number.

christophe@pallier.org
If you use this script, please cite us (and expyriment!).

