The script `scramble-files` calls the function `grains2` on the files 'phXXX.wav' in the current directory, scrambling the energy in different frequency bands. 

It must adapted if the wav files have different name pattern.

If used with Octave rather than Matlab, one must type:

     pkg load signal

Before executing the script.

The parameters twin=200 and trand=1000 are suitable to destroy intelligility.

NOTE: these scripts were written by [Daniel Pressnitzer](https://lsp.dec.ens.fr/en/member/661/daniel-pressnitzer) and used in the research reported in: 

Joly, Olivier, Christophe Pallier, Franck Ramus, Daniel Pressnitzer, Wim Vanduffel, and Guy A. Orban. 2012. “Processing of Vocalizations in Humans and Monkeys: A Comparative FMRI Study.” NeuroImage 62 (3): 1376–89. https://doi.org/10.1016/j.neuroimage.2012.05.070.

Here is the desciption of the algorithm:

"Scrambled sounds were made by processing all individual (intact) stimuli through a gammatone filterbank (Patterson et al. 1995) with 64 channels. As in Patterson et al. (1995), the filterbank was chosen to mimic human frequency selectivity. The equivalent rectangular bandwidth (ERB) of each channel was thus set to ERB = 24.7(1+4.37F), with F being the center frequency in kHz. In each channel, the signal was windowed with overlapping Hanning windows of 25-ms duration. The windows were then shuffled randomly within a channel, with the additional constraint that a window could be displaced by no more than ±500 ms from its original temporal position. The scrambled signals were finally obtained by putting all frequency channels back together."

christophe@pallier.org
05/03/2018


