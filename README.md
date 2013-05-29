INF
============

This model simulates a group of neurons which act in accordance to integrate-and-fire differential equations.  The simulation proceeds in a novel manner, data being stored in matrices and arrays for the following variables:
http://www.neurdon.com/2011/03/06/spiking-neural-networks-in-python-part-1/
http://www.neurdon.com/2011/03/06/spiking-neural-networks-in-python-part-3/

The states of the neuronal model will be used to control music synthesis via Python via
http://www.swharden.com/blog/2011-07-08-create-mono-and-stereo-wave-files-with-python/

TODO:
introduce dynamic matrix size control such that the time series can be infinite (i.e. a while loop) instead of predefined.  
figure out how to analyze the matrices and arrays to output meaningful sound combinations