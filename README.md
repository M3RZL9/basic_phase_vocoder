# basic_phase_vocoder
Made for vk
# What it does
Stretches or shortens the audio .wav file without chaning the pitch
# How it works:
basic_phase_vocoder.py input_file.wav output_file.wav N
where N is the algorithm parameter, 0 < N < 1 to shorten, 1 < N to stretch 
based on https://web.archive.org/web/20160914202340/https://audioprograming.wordpress.com/2012/03/02/a-phase-vocoder-in-python/
