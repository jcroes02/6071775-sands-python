import matplotlib.pyplot as plt
import numpy as np
from gen_waves import *
from operation import *

A=1
F=2
d=10
s_r=100
L=3

t,signal = gen_square_signal(A,F,d,s_r)
t,signal2 = gen_stepl(A,L,d,s_r)

time_shifted_wave = time_shift(signal, 5, s_r)

time_scaled_wave = time_scale(signal, 3)

amplitude_scaled_wave = amplitude_shift(signal, 4)

added_wave = add_signals(signal, signal2)

multiplied_wave = multiply_signals(signal, time_scaled_wave)

fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)
ax1.plot(signal)
ax2.plot(added_wave)

plt.show()