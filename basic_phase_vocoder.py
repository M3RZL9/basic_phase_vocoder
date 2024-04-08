import numpy as np
import sys
import pylab 
from scipy.io import wavfile

N = 2048
H = N/4

# read input and get the timescale factor
(sr,signalin) = wavfile.read(sys.argv[1])
L = len(signalin)
tscale = 1 / float(sys.argv[3])
# signal blocks for processing and output
phi  = np.zeros(N)
out = np.zeros(N, dtype=complex)
sigout = np.zeros(int(L/tscale+N))

# max input amp, window
amp = max(signalin)
win = np.hanning(N)
p = 0
pp = 0

while p < L-(N+H):

# take the spectrum of two consecutive windows
    p1 = int(p)
    H1 = int(H)
    spec1 =  np.fft.fft(win*signalin[p1:p1+N])
    spec2 =  np.fft.fft(win*signalin[p1+H1:p1+N+H1])
    # take their phase difference and integrate
    phi += (np.angle(spec2) - np.angle(spec1))
    # bring the phase back to between pi and -pi
    for i in phi:
        while i > pylab.pi:
            i -= 2*pylab.pi
        while i <= -pylab.pi:
            i += 2*pylab.pi
    out.real, out.imag = pylab.cos(phi), pylab.sin(phi)
    # inverse FFT and overlap-add
    sigout[int(pp):int(pp+N)] = sigout[int(pp):int(pp+N)] + win*np.fft.ifft(abs(spec2)*out).real 

    pp += H
    p += H*tscale


#  write file to output, scaling it to original amp

wavfile.write(sys.argv[2],sr,np.array(amp*sigout/max(sigout), dtype='int16'))
