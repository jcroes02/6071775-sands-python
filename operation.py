import matplotlib.pyplot as plt
from gen_waves import *
#sine wave
A=2
F=5
duration=1
sample_rate=200

sine=gen_sine_wave(A,F,duration,sample_rate)

#square wave
A=2
F=5
duration=1
sample_rate=200

square=gen_square_signal(A,F,duration,sample_rate)

#sawtooth
A=2
F=5
duration=1
sample_rate=1000

sawtooth=gen_sawtooth_signal(A,F,duration,sample_rate)

#unit step
A=2
S=-10
E=10
L=5
sample_rate=500

step=gen_step(A,L,S,E,sample_rate)